from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True, blank=True,
                               related_name='children')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    amount = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField()
    category = models.ForeignKey(Catalog, on_delete=models.SET_DEFAULT, default=None)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    rating = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name



