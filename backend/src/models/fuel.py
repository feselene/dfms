from django.db import models
from .vehicle import Vehicle

class Fuel(models.Model):
    FUEL_CHOICES = [
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('petrol', 'Petrol'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    amount = models.DecimalField(max_digits=6, decimal_places=2)  # Liters or equivalent units
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.amount} {self.fuel_type} for {self.vehicle}"
