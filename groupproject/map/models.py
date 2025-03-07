from django.db import models


class Location(models.Model):
    """Attributes of Location table"""
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    qr_code = models.ImageField(upload_to='qr_codes/')
    qr_code_message = models.CharField(max_length=255)
    challengeId = models.IntegerField(default=0)
    locationId = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
