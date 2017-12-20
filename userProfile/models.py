from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.city


class User(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    age = models.CharField(max_length=2)
    image = models.CharField(max_length=1000)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

