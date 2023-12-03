from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrackViewSet, ArtistViewSet, AlbumViewSet, GenreViewSet, root_redirect

# Creating a router and registering our viewsets with it.
router = DefaultRouter()

router.register(r'tracks', TrackViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'genres', GenreViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', root_redirect, name='root-redirect'),
    path('', include(router.urls)),
]



















# from django.urls import path, include, re_path
# from rest_framework import permissions
#
# from .views import MaterialViewSet
# from rest_framework.routers import DefaultRouter
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#
#
#
# #
# router = DefaultRouter()
# router.register('track', MaterialViewSet)
#
# urlpatterns = [
#    path('', include(router.urls)),
# ]
