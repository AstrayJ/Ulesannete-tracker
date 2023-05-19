from django.db import models

class Event(models.Model):
    Sündmus= models.CharField(max_length=100)
    Lisa = models.CharField(max_length=150)
    Olulisus= models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    Algus kuupäev= models.DateField()
    Lõpp kuupäev= models.DateField()