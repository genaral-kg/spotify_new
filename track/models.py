from django.db import models
from django.core import validators

class Genre(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='Genre')
    description = models.TextField(blank=True, null=True)  # Optional: add a description field

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.title
class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField()

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return f"{self.title} by {self.artist.name}"


class Track(models.Model):
    title = models.CharField(max_length=30, unique=True)
    year = models.SmallIntegerField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)  # New field for artist
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True)  # New field for album
    audio_file = models.FileField(upload_to='tracks/', blank=True, validators=[validators.FileExtensionValidator(['mp3', 'wav'], message='File must be an audio file')])
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='tracks')


    def __str__(self):
        return self.title









































# class Material(models.Model):
#     title = models.CharField(max_length=30, unique=True)
#     year = models.SmallIntegerField(blank=True, null=True)
#     desc = models.TextField(blank=True, null=True)
#     category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
#     image = models.ImageField(upload_to='media/', blank=True)
#     video = models.FileField(upload_to='media/', blank=True, validators=[validators.FileExtensionValidator(['mp4'], message='file must be mp3')])
# class Category(models.Model):
#     title = models.CharField(max_length=30, unique=True, verbose_name='Category')
#     image = models.ImageField(upload_to='media/', blank=True)
#
#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'
#
#
#     def __str__(self):
#         return self.title


