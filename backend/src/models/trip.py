from django.db import models
from .vehicle import Vehicle
from .driver import Driver

class Trip(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')

    def __str__(self):
        return f"Trip {self.id} - {self.status}"
