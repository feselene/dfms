from django.db import models

class Route(models.Model):
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    stops = models.TextField(blank=True, null=True)  # JSON string for stops or use a JSONField if supported
    estimated_time = models.DurationField()
    distance = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Route from {self.start_location} to {self.end_location}"
