from rest_framework import permissions, viewsets, response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rating.serializers import ReviewSerializer

from .models import Track, Artist, Album, Genre
from .serializers import (
    TrackListSerializer, TrackDetailSerializer, TrackCreateSerializer,
    ArtistSerializer, AlbumSerializer, GenreSerializer)
from django.shortcuts import redirect

def root_redirect(request):
    return redirect('/admin/')  # Redirects to the admin page



class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'artist__name', 'album__title', 'genre__title')
    filterset_fields = ('genre', 'artist', 'album')

    def get_serializer_class(self):
        if self.action == 'list':
            return TrackListSerializer
        elif self.action == 'retrieve':
            return TrackDetailSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return TrackCreateSerializer
        return TrackListSerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    # Assuming you have a Review model and serializer
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        track = self.get_object()
        reviews = track.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return response.Response(serializer.data)

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]











