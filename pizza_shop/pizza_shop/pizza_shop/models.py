# from django.db import models
#
# class Card(models.Model):
#     title = models.CharField(max_length=30)
#     desc = models.CharField(max_length=30)
#     price = models.IntegerField(max_length=30)
#     img = models.ImageField(upload_to='/index/')

from django.db import models

class PizzaCard(models.Model):
    # name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='index/')
    title = models.CharField(max_length=200)  # Новое поле для заголовка

    def __str__(self):
        return self.name

