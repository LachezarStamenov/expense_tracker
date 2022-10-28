from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from expense_tracker_app.expense_tracker.validators import MaxFileSizeInMbValidator, only_letters_validator


class Profile(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=15, validators=(MinLengthValidator(2), only_letters_validator))
    last_name = models.CharField(verbose_name='Last Name', max_length=15, validators=(MinLengthValidator(2), only_letters_validator))
    budget = models.FloatField(default=0, validators=(MinValueValidator(0),))
    profile_image = models.ImageField(
        verbose_name='Profile Image',
        upload_to='profiles/',
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(5),
        ),
    )


class Expense(models.Model):
    title = models.CharField(max_length=30)
    expense_image = models.URLField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
