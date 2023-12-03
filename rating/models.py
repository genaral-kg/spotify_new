from django.db import models
from track.models import Track
from django.contrib.auth import get_user_model

User = get_user_model()

class Review(models.Model):
    RATING_CHOICES = [
        (1, 'Not my taste'),
        (2, 'Could be better'),
        (3, 'Average'),
        (4, 'Enjoyable'),
        (5, 'Outstanding')
    ]

    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']
        unique_together = ('track', 'owner')  # Ensures a user can only review a track once

    def __str__(self):
        return f'{self.track.title} Review by {self.owner.username}'
