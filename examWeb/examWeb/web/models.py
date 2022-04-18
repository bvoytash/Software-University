import re

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator
from django.db import models

def validate_username(value):
    if not re.match("^[A-Za-z0-9_]*$", value):
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


class Profile(models.Model):
    MIN_AGE = 0

    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            validate_username,
        )
    )

    email = models.EmailField()

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=(
            MinValueValidator(MIN_AGE),
        ),
    )


class Album(models.Model):
    MIN_PRICE = float(0)

    CHOICES = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    )

    album_name = models.CharField(
        max_length=30,
        unique=True
    )
    artist = models.CharField(
        max_length=30
    )
    genre = models.CharField(
        max_length=30,
        choices=CHOICES
    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(MinValueValidator(MIN_PRICE),),
    )

