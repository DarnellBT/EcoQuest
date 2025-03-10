from django.db import models


class Location(models.Model):
    """Attributes of Location table"""
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    icon = models.CharField(max_length=255)
    locationId = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
