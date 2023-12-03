from rest_framework import serializers
from .models import Track, Genre, Artist, Album


# class CategorySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Category
#         fields = '__all__'
#
#
# class MaterialListSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Material
#         fields = ('title', 'year', 'category')
#
#
# class MaterialDetailSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Material
#         fields = '__all__'
#
#
# class MaterialCreateSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Material
#         fields = ('title', 'year', 'video', 'desc', 'image', 'category')
# +++  NEW  +++
# ----------------------------***********------------------------
# GENRE serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
# -----------------------------

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

# Track list concrete
class TrackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('title', 'year', 'genre', 'artist', 'album')

# Detail
class TrackDetailSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Track
        fields = '__all__'


class TrackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('title', 'year', 'audio_file', 'desc', 'image', 'genre', 'artist', 'album')





