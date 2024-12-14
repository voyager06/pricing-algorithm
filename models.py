from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

class WeatherCondition(models.Model):
    temperature = models.FloatField()
    rain = models.FloatField()
    is_busy = models.BooleanField()
