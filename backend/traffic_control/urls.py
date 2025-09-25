from django.urls import path
from .views import StationListAPIView, TrainListAPIView

urlpatterns = [
    path('stations/', StationListAPIView.as_view(), name='station-list'),
    path('trains/', TrainListAPIView.as_view(), name='train-list'),
]