from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    