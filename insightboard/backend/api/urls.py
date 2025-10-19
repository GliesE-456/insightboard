from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DailyLogViewSet, InsightViewSet

router = DefaultRouter()
router.register(r'dailylogs', DailyLogViewSet)
router.register(r'insights', InsightViewSet)

urlpatterns = [
    path('', include(router.urls)),
]