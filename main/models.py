from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    world = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=255)
    birth_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='birth_location')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='current_location')
    description = models.TextField()
    image = models.ImageField(upload_to='photos/')
    GENDER = (
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ('unknown', 'Неизвестно')
    )
    gender = models.CharField(max_length=10, choices=GENDER)
    race = models.CharField(max_length=55)
    DEAD = (
        ('dead', 'Мертвый'),
        ('alive', 'Живой')
    )
    dead = models.CharField(max_length=10, choices=DEAD)

    def __str__(self):
        return self.name


class Episode(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    number_season = models.IntegerField()
    image = models.ImageField(upload_to='photos/')
    description = models.TextField()
    premiere = models.DateField()
    character = models.ManyToManyField(Character, related_name='char_to_ep')

    def __str__(self):
        return f"{self.number_season} + {self.number}"
