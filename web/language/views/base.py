import sys

from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from rest_framework import viewsets, generics, mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from users.models import User, Administrator
from language.models import (
    CommunityMember,
    PlaceName
)

class BaseModelViewSet(viewsets.ModelViewSet):
    """
    Abstract base viewset that allows multiple serializers depending on action.
    """

    def get_serializer_class(self):
        if self.action != "list":
            if hasattr(self, "detail_serializer_class"):
                return self.detail_serializer_class

        return super().get_serializer_class()


class BasePlaceNameListAPIView(generics.ListAPIView):
    """
    Abstract list API view that allows multiple serializers.

    1) If NO USER is logged in, only shows VERIFIED, UNVERIFIED or NULL status content
    2) If USER IS LOGGED IN, show:
        2.1) User's contribution regardless the status
        2.2) User's community_only content from user's communities. Rules:
            2.2.1) Is NOT COMMUNITY ONLY (False or NULL) but status is VERIFIED, UNVERIFIED or NULL
            2.2.2 Is COMMUNITY ONLY
        2.3) Everything from where user is Administrator (language/community pair)
    
    Note: Users can contribute this data, so never cache it.
    """

    @method_decorator(never_cache)
    def list(self, request):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        user_logged_in = False
        if request and hasattr(request, "user"):
            if request.user.is_authenticated:
                user_logged_in = True

        if user_logged_in:
            # Rule 2.1
            queryset_user = queryset.filter(creator__id=request.user.id)

            # Rule 2.2
            user_communities = CommunityMember.objects.filter(
                user__id=int(request.user.id)
            ).filter(
                status__exact=CommunityMember.VERIFIED
            ).values('community')

            # Specifically Rules 2.2.1 and 2.2.2
            queryset_community = queryset.filter(
                Q(community_only=False, status__exact=PlaceName.VERIFIED)
                | Q(community_only=False, status__exact=PlaceName.UNVERIFIED)
                | Q(community_only=False, status__isnull=True)
                | Q(community_only__isnull=True, status__exact=PlaceName.VERIFIED)
                | Q(community_only__isnull=True, status__exact=PlaceName.UNVERIFIED)
                | Q(community_only__isnull=True, status__isnull=True)
                | Q(community__in=user_communities)
            )

            # Rule 2.3
            admin_languages = Administrator.objects.filter(
                user__id=int(request.user.id)).values('language')
            admin_communities = Administrator.objects.filter(
                user__id=int(request.user.id)).values('community')

            if admin_languages and admin_communities:
                # Filter PlaceNames by admin's languages
                queryset_admin = queryset.filter(
                    language__in=admin_languages, community__in=admin_communities
                )
                if queryset_admin:
                    queryset = queryset_user.union(
                        queryset_community).union(queryset_admin)
                else:
                    queryset = queryset_user.union(queryset_community)
            else:  # user is not Administrator of anything
                queryset = queryset_user.union(queryset_community)

        else:  # User is not authenticated
            queryset = queryset.filter(
                Q(status__exact=PlaceName.VERIFIED)
                | Q(status__exact=PlaceName.UNVERIFIED)
                | Q(status__isnull=True)
            )

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
