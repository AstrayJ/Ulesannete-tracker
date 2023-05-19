from django.db import models

class Event(models.Model):
    Sündmus= models.CharField(max_length=100)

    Olulisus= models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    Kuupäev= models.DateField(_(""), auto_now=False, auto_now_add=False)

    Lisa = models.CharField(max_length=150)

    Olulisus= models.IntegerField()
    Alguskuupäev= models.DateField()
    Lõppkuupäev= models.DateField()

    Olulisus= models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )


