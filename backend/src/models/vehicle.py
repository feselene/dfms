from django.db import models

class Vehicle(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('in_transit', 'In Transit'),
        ('maintenance', 'Maintenance'),
        ('out_of_service', 'Out of Service'),
    ]

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()  # Passenger or cargo capacity
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    location = models.CharField(max_length=100, blank=True, null=True)  # GPS or address

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - {self.status}"
