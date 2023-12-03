from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ReviewViewSet

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    # ... other url patterns ...
    path('', include(router.urls)),
]
