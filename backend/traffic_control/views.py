from rest_framework import generics
from .models import Station, Train
from .serializers import StationSerializer, TrainSerializer

# Create your views here.
class StationListAPIView(generics.ListAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class TrainListAPIView(generics.ListAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer