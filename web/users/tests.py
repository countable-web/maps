from rest_framework.test import APITestCase
from rest_framework import status

from language.models import Language, Community
from users.models import User


class UserAPITests(APITestCase):
    def setUp(self):
        self.language1 = Language.objects.create(name="Test language 001")
        self.language2 = Language.objects.create(name="Test language 002")
        self.community1 = Community.objects.create(name="Test community 001")
        self.community2 = Community.objects.create(name="Test community 002")

        self.user = User.objects.create(
            username="testuser001",
            first_name="Test",
            last_name="user 001",
            email="test@countable.ca",
        )
        self.user.set_password("password")
        self.user.languages.add(self.language1)
        self.user.languages.add(self.language2)
        self.user.communities.add(self.community1)
        self.user.save()

    ###### ONE TEST TESTS ONLY ONE SCENARIO ######

    def test_user_detail_route_exists(self):
        """
        Ensure user Detail API route exists
        """
        self.client.login(username="testuser001", password="password")
        response = self.client.get(
            "/api/user/{}".format(self.user.id), format="json", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_detail(self):
        """
        Ensure we can retrieve a newly created user object.
        """
        self.client.login(username="testuser001", password="password")
        response = self.client.get(
            "/api/user/{}/".format(self.user.id), format="json", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.user.id)
        self.assertEqual(len(response.data["languages"]), 2)
        self.assertEqual(len(response.data["communities"]), 1)

    def test_user_post_not_allowed(self):
        """
        Ensure there is no user create API
        """
        response = self.client.post(
            "/api/user/",
            {
                "username": "testuser001",
                "first_name": "Test",
                "last_name": "user 001",
                "email": "test@countable.ca",
            },
            format="json",
        )
        self.assertEqual(response.status_code,
                         status.HTTP_404_NOT_FOUND)

    def test_user_set_community(self):
        """
        Check we can set the community
        """
        # TODO: test I can't edit without logging in.
        self.client.login(username="testuser001", password="password")
        response = self.client.patch(
            "/api/user/{}/".format(self.user.id),
            {"community_ids": [self.community2.id, self.community1.id]},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check updates are reflected in API.
        response = self.client.get(
            "/api/user/{}/".format(self.user.id), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.user.id)
        self.assertEqual(len(response.data["languages"]), 2)
        self.assertEqual(len(response.data["communities"]), 2)

    def test_user_patch(self):
        """
        Check we can set the bio on the user's settings page.
        """
        self.client.login(username="testuser001", password="password")
        response = self.client.patch(
            "/api/user/{}/".format(self.user.id), {"bio": "bio"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(
            "/api/user/{}/".format(self.user.id), format="json")
        self.assertEqual(response.data["bio"], "bio")
