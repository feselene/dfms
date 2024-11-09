from django.db import models

class Driver(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('on_trip', 'On Trip'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    license_number = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.name
