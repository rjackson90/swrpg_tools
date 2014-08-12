from django.db import models

class Map(models.Model):
    str_id = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to="map/%Y/%m/%d")
