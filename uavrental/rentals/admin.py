from django.contrib import admin
from .models import UAV, Rental


@admin.register(UAV)
class UAVAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'weight', 'category')  # Listede hangi alanların görüntüleneceğini belirtiyoruz


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('uav', 'date_from', 'date_to', 'renting_member')  # Listede hangi alanların görüntüleneceğini belirtiyoruz
