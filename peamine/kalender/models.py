from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    Sundmus= models.CharField(max_length=100)

    Olulisus= models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    Kuupaev= models.DateField(_(""), auto_now=False, auto_now_add=False)

    Lisa = models.CharField(max_length=150)

    Olulisus= models.IntegerField()
    Alguskuupaev= models.DateField()
    Loppkuupaev= models.DateField()

    Olulisus= models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )


