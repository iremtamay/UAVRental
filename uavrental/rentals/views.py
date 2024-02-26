from rest_framework import generics
from .models import UAV, Rental
from .serializers import UAVSerializer, RentalSerializer

class UAVListCreateAPIView(generics.ListCreateAPIView):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer

class UAVRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer

class RentalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

class RentalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

