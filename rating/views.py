from rest_framework import viewsets, permissions

from rating.models import Review
from rating.serializers import CreateUpdateReviewSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Modify as needed

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateUpdateReviewSerializer
        return ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
