from django.contrib import admin
from .models import Genre, Track, Artist, Album

admin.site.register(Genre)
admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(Album)
