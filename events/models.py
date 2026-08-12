from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to="events/", blank=True, null=True)
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title