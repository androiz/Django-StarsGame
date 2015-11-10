from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Thematic(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=20, unique=True)
    thematic = models.ForeignKey(Thematic)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=False, unique=True)
    race = models.ForeignKey(Race, null=False, unique=False)
    thematic = models.ForeignKey(Thematic)
    zonaX = models.IntegerField()
    zonaY = models.IntegerField()

    def __str__(self):
        return str(self.user)


class Unit(models.Model):
    name = models.CharField(max_length=20, unique=True)
    race = models.ForeignKey(Race, null=False, unique=False)
    thematic = models.ForeignKey(Thematic)

    def __str__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=20, unique=True)
    race = models.ForeignKey(Race, null=False, unique=False)
    thematic = models.ForeignKey(Thematic)

    def __str__(self):
        return self.name

class GeneralTechnology(models.Model):
    name = models.CharField(max_length=20, unique=True)
    thematic = models.ForeignKey(Thematic)

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=100, null=False, unique=False)
    thematic = models.ForeignKey(Thematic)

    def __str__(self):
        return self.name

class RelationResourcesUsers(models.Model):
    user = models.ForeignKey(UserProfile, null=False, unique=False)
    resource = models.ForeignKey(Resource, null=False, unique=False)
    amoung = models.FloatField()

class RelationUnitsUsers(models.Model):
    user = models.ForeignKey(UserProfile, null=False, unique=False)
    unit = models.ForeignKey(Unit, null=False, unique=False)
    amoung = models.IntegerField()

class RelationBuildingsUsers(models.Model):
    user = models.ForeignKey(UserProfile, null=False, unique=False)
    building = models.ForeignKey(Building, null=False, unique=False)
    amoung = models.IntegerField()

class RelationGeneralTechnologiesUsers(models.Model):
    user = models.ForeignKey(UserProfile, null=False, unique=False)
    technology = models.ForeignKey(GeneralTechnology, null=False, unique=False)
    level = models.IntegerField()