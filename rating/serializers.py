from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Changed from email to username
    track = serializers.ReadOnlyField(source='track.title')

    class Meta:
        model = Review
        fields = "__all__"

class CreateUpdateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['track', 'rating', 'text']  # 'track' accepts track ID
