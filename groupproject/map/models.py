from django.db import models


class Location(models.Model):
    locationId = models.BigAutoField(primary_key=True) 
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(decimal_places=17, max_digits=25)
    longitude = models.DecimalField(decimal_places=17, max_digits=25)
    qr_code = models.ImageField(default='NULL', upload_to='./map/static')
    qr_code_message = models.CharField(default='NULL', max_length=50)
    task = models.CharField(default='NULL', max_length=20, null=False)
