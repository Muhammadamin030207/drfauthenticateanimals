from django.db import models
from django.utils.text import slugify


class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    airline = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    departure_airport = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100)
    departure_country = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_airport = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    arrival_country = models.CharField(max_length=100)
    arrival_time = models.DateTimeField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    aircraft_type = models.CharField(max_length=50)
    economy_price = models.DecimalField(max_digits=10, decimal_places=2)
    business_price = models.DecimalField(max_digits=10, decimal_places=2)
    first_class_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[
        ('scheduled', 'Scheduled'),
        ('boarding', 'Boarding'),
        ('departed', 'Departed'),
        ('arrived', 'Arrived'),
        ('cancelled', 'Cancelled'),
        ('delayed', 'Delayed'),
    ], default='scheduled')
    baggage_allowance = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'flights_flight'
        ordering = ['departure_time']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.flight_number}-{self.airline}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.flight_number} ({self.airline})"