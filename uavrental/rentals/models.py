from django.db import models

class UAV(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight = models.FloatField()
    category = models.CharField(max_length=50)
   

    def __str__(self):
        return f"{self.brand} {self.model}"

class Rental(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    renting_member = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.uav} - {self.renting_member}"
