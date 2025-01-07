from django.db import models


class Buyer (models.Model):
    name = models.CharField(max_length=150)
    balance = models.DecimalField(decimal_places=2, max_digits=10) # 2 знака после запятой, максимум 10 символов.
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    size = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(default="Очень хорошая игра")
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title









# Create your models here.
