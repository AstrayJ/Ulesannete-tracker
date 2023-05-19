from django.db import models

class Event(models.Model):
    Sündmus= models.CharField(max_length=100)
<<<<<<< HEAD
    Olulisus= models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    Kuupäev= models.DateField(_(""), auto_now=False, auto_now_add=False)
=======
    Lisa = models.CharField(max_length=150)
    Olulisus= models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    Algus kuupäev= models.DateField()
    Lõpp kuupäev= models.DateField()
>>>>>>> f726452b778ad5e6e15ee4fe5a4249665ad5befb
