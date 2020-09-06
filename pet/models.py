from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    #fixed to the admin view
    def __str__(self):

        return self.name
