  
from django.db import models

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

# Add the new Train model below
class Train(models.Model):
    train_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    current_station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, blank=True, related_name='trains_at_station')
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='trains_heading_to')

    def __str__(self):
        return self.name