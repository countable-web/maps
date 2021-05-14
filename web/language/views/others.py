from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from web.utils import is_user_permitted
from language.models import (
    Favourite,
    Notification,
    Recording,
)
from language.views import BaseModelViewSet
from language.serializers import (
    FavouriteSerializer,
    NotificationSerializer,
    RecordingSerializer,
)
from language import statics



class RecordingViewSet(BaseModelViewSet):
    serializer_class = RecordingSerializer
    queryset = Recording.objects.all()


class NotificationViewSet(BaseModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @method_decorator(never_cache)
    def list(self, request):
        queryset = self.get_queryset()
        
        if request and hasattr(request, "user"):
            if request.user.is_authenticated:
                queryset = queryset.filter(user__id = request.user.id)
                serializer = self.serializer_class(queryset, many=True)
                return Response(serializer.data)        

        return Response({"message": statics.ERROR_LOGIN_REQUIRED}, 
                        status=status.HTTP_401_UNAUTHORIZED)


# To enable only CREATE and DELETE, we create a custom ViewSet class...
class FavouriteCustomViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    pass


class FavouriteViewSet(FavouriteCustomViewSet, GenericViewSet):
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @method_decorator(login_required)
    def create(self, request, *args, **kwargs):
        if 'place' in request.data.keys() or 'media' in request.data.keys():

            if 'media' in request.data.keys():
                media_id = int(request.data["media"])

                # Check if the favourite already exists
                if Favourite.favourite_media_already_exists(request.user.id, media_id):
                    return Response({"message": "This media is already a favourite"}, 
                                    status=status.HTTP_409_CONFLICT)
                else:
                    return super(FavouriteViewSet, self).create(request, *args, **kwargs)

            if 'place' in request.data.keys():
                placename_id = int(request.data["place"])

                # Check if the favourite already exists
                if Favourite.favourite_place_already_exists(request.user.id, placename_id):
                    return Response({"message": "This placename is already a favourite"}, 
                                    status=status.HTTP_409_CONFLICT)
                else:
                    return super(FavouriteViewSet, self).create(request, *args, **kwargs)
        else:
            return super(FavouriteViewSet, self).create(request, *args, **kwargs)
    
    def retrieve(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        if is_user_permitted(request, instance.user.id):
            return super().retrieve(request)
        
        return Response(
            {'message': statics.ERROR_UNAUTHORIZED_USER},
            status=status.HTTP_401_UNAUTHORIZED
        )

    def destroy(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        if is_user_permitted(request, instance.user.id):
            return super().destroy(request)
        
        return Response(
            {'message': statics.ERROR_UNAUTHORIZED_USER},
            status=status.HTTP_401_UNAUTHORIZED
        )

    @method_decorator(never_cache)
    def list(self, request):
        queryset = self.get_queryset()
        
        if request and hasattr(request, "user"):
            if request.user.is_authenticated:
                queryset = queryset.filter(user__id = request.user.id)
                serializer = self.serializer_class(queryset, many=True)
                return Response(serializer.data)
        return Response([])
