from django.db import models
from .vehicle import Vehicle
from .driver import Driver

class Alert(models.Model):
    TYPE_CHOICES = [
        ('maintenance_due', 'Maintenance Due'),
        ('accident_reported', 'Accident Reported'),
        ('route_change', 'Route Change'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    alert_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=[('new', 'New'), ('acknowledged', 'Acknowledged'), ('resolved', 'Resolved')], default='new')

    def __str__(self):
        return f"Alert {self.alert_type} for {self.vehicle or self.driver}"
