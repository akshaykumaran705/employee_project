from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, PerformanceViewSet, charts_view

router = DefaultRouter()
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('charts/', charts_view, name='charts'),
]
