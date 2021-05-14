import sys

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import action

from web.permissions import IsAdminOrReadOnly
from users.models import User
from language.views import BaseModelViewSet
from language.models import (
    Language,
    Recording,
)
from language.serializers import (
    LanguageGeoSerializer,
    LanguageSerializer,
    LanguageDetailSerializer,
    LanguageSearchSerializer
)
from language import statics


class LanguageViewSet(BaseModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = LanguageSerializer
    detail_serializer_class = LanguageDetailSerializer
    queryset = (
        Language.objects.filter(geom__isnull=False)
        .select_related("family")
        .order_by("family", "name")
    )

    @method_decorator(never_cache)
    def detail(self, request):
        return super().detail(request)

    @action(detail=True, methods=["patch"])
    def add_language_audio(self, request, pk):
        if 'recording_id' not in request.data.keys():
            return Response({"message": statics.ERROR_NO_RECORDING})
        if not pk:
            return Response({"message": statics.ERROR_NO_LANGUAGE})

        recording_id = int(request.data["recording_id"])
        language_id = int(pk)
        language = Language.objects.get(pk=language_id)
        recording = Recording.objects.get(pk=recording_id)
        language.language_audio = recording
        language.save()

        return Response({"message": "Language audio associated."},
                        status=status.HTTP_200_OK)

    @action(detail=True, methods=["patch"])
    def add_greeting_audio(self, request, pk):
        if 'recording_id' not in request.data.keys():
            return Response({"message": statics.ERROR_NO_RECORDING})
        if not pk:
            return Response({"message": statics.ERROR_NO_LANGUAGE})

        recording_id = int(request.data["recording_id"])
        language_id = int(pk)
        language = Language.objects.get(pk=language_id)
        recording = Recording.objects.get(pk=recording_id)
        language.greeting_audio = recording
        language.save()

        return Response({"message": "Greeting audio associated."},
                        status=status.HTTP_200_OK)

    def create_membership(self, request):
        user_id = int(request.data["user"]["id"])
        language_id = int(request.data["language"]["id"])
        language = Language.objects.get(pk=language_id)
        user = User.objects.get(pk=user_id)
        user.languages.add(language)
        user.save_m2m()
        # TODO: use relationship here instead.
        # if LanguageMember.member_exists(user_id, language_id):
        #     return Response({"message", "User is already a language member"})
        # else:
        #     member = LanguageMember.create_member(user_id, language_id)
        #     serializer = LanguageMemberSerializer(member)
        #     return Response(serializer.data)


# Geo List APIViews
class LanguageGeoList(generics.ListAPIView):
    queryset = Language.objects.filter(geom__isnull=False)
    serializer_class = LanguageGeoSerializer

    @method_decorator(never_cache)
    def list(self, request):
        return super().list(request)


# Search List APIViews
class LanguageSearchList(generics.ListAPIView):
    queryset = Language.objects.filter(geom__isnull=False)
    serializer_class = LanguageSearchSerializer

    @method_decorator(never_cache)
    def list(self, request):
        return super().list(request)
