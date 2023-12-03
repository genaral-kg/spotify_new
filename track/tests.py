# tests.py in your Django app

from django.test import TestCase
from .models import Genre, Artist, Album, Track
from django.utils import timezone

class GenreModelTest(TestCase):

    def test_genre_creation(self):
        genre = Genre.objects.create(title="Rock")
        self.assertEqual(genre.title, "Rock")

class ArtistModelTest(TestCase):

    def test_artist_creation(self):
        artist = Artist.objects.create(name="John Doe")
        self.assertEqual(artist.name, "John Doe")

class AlbumModelTest(TestCase):

    def test_album_creation(self):
        artist = Artist.objects.create(name="John Doe")
        album = Album.objects.create(title="Album One", artist=artist, release_date=timezone.now())
        self.assertEqual(album.title, "Album One")
        self.assertEqual(album.artist.name, "John Doe")

class TrackModelTest(TestCase):

    def test_track_creation(self):
        genre = Genre.objects.create(title="Rock")
        artist = Artist.objects.create(name="John Doe")
        album = Album.objects.create(title="Album One", artist=artist, release_date=timezone.now())
        track = Track.objects.create(title="Song One", artist=artist, album=album, genre=genre, year=2021)
        self.assertEqual(track.title, "Song One")
        self.assertEqual(track.artist.name, "John Doe")
        self.assertEqual(track.album.title, "Album One")
        self.assertEqual(track.genre.title, "Rock")
        self.assertEqual(track.year, 2021)


#Testing ViewSets

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

class TrackViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.genre = Genre.objects.create(title="Rock")
        self.artist = Artist.objects.create(name="John Doe")
        self.album = Album.objects.create(title="Album One", artist=self.artist, release_date=timezone.now())
        self.track_data = {
            'title': 'Song One',
            'artist': self.artist.id,
            'album': self.album.id,
            'genre': self.genre.id,
            'year': 2021
        }

    def test_create_track(self):
        response = self.client.post('/api/tracks/', self.track_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Track.objects.count(), 1)
        self.assertEqual(Track.objects.get().title, 'Song One')

    def test_get_track_list(self):
        Track.objects.create(title="Song One", artist=self.artist, album=self.album, genre=self.genre, year=2021)
        response = self.client.get('/api/tracks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
