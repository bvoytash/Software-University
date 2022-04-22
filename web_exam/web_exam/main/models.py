from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    MIN_AGE = 12

    email = models.EmailField()

    age = models.IntegerField(
        validators=(
            MinValueValidator(MIN_AGE),
        ),
    )

    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)


class Game(models.Model):
    CHOICES = (
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other"),
    )

    title = models.CharField(max_length=30, unique=True)
    category = models.CharField(max_length=15, choices=CHOICES)
    rating = models.FloatField(validators=(MinValueValidator(0.1), MaxValueValidator(5.0),),)
    max_level = models.IntegerField(validators=(MinValueValidator(1),), blank=True, null=True, )
    image = models.URLField()
    summary = models.TextField(blank=True, null=True)
