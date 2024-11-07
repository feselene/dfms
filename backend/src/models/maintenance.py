from django.db import models
from .vehicle import Vehicle

class Maintenance(models.Model):
    TYPE_CHOICES = [
        ('oil_change', 'Oil Change'),
        ('brake_repair', 'Brake Repair'),
        ('tire_rotation', 'Tire Rotation'),
        ('inspection', 'Inspection'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()
    maintenance_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.maintenance_type} on {self.vehicle}"
