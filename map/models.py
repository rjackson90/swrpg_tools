from django.db import models

class Map(models.Model):
    str_id = models.SlugField(max_length=60, unique=True, db_index=True, blank=True)
    title = models.CharField(max_length=60, blank=True)
    image = models.ImageField(upload_to="map/%Y/%m/%d")

class Character(models.Model):
    # Basic info
    slug = models.SlugField(max_length=60, unique=True, db_index=True, blank=True)
    name = models.CharField(max_length=60)
    portrait = models.ImageField(upload_to="map/%Y/%m/%d")

    # Stats
    wound_threshold = models.PositiveSmallIntegerField()
    strain_threshold = models.PositiveSmallIntegerField()
    wounds = models.PositiveSmallIntegerField()
    strain = models.PositiveSmallIntegerField()

class Encounter(models.Model):
    slug = models.SlugField(max_length=60, unique=True, db_index=True, blank=True)
    name = models.CharField(max_length=60)
    scene = models.ForeignKey("Map")
    characters = models.ManyToManyField('Character')
