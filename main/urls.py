"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from favorites.views import FavoriteViewSet
from rating.views import ReviewViewSet
from track.views import TrackViewSet, ArtistViewSet, AlbumViewSet, GenreViewSet

# Swagger schema view setup
schema_view = get_schema_view(
    openapi.Info(
        title="Spotify api test project from Kutman",
        default_version='v1',
        description="Test REST API backend at django",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# API Router
router = DefaultRouter()
router.register('tracks', TrackViewSet)
router.register('artists', ArtistViewSet)
router.register('albums', AlbumViewSet)
router.register('genres', GenreViewSet)
router.register('favorites', FavoriteViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # API URLs
    path('api/v1/', include(router.urls)),
    path('api/v1/accounts/', include('account.urls')),
    path('filter/', include('track.urls')),

    # Swagger Documentation
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Serving media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
