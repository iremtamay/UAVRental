"""
URL configuration for uavrental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import UAVListCreateAPIView, UAVRetrieveUpdateDestroyAPIView, RentalListCreateAPIView, RentalRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('uavs/', UAVListCreateAPIView.as_view(), name='uav-list-create'),
    path('uavs/<int:pk>/', UAVRetrieveUpdateDestroyAPIView.as_view(), name='uav-detail'),
    path('rentals/', RentalListCreateAPIView.as_view(), name='rental-list-create'),
    path('rentals/<int:pk>/', RentalRetrieveUpdateDestroyAPIView.as_view(), name='rental-detail'),
]

