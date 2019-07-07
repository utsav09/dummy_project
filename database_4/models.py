from django.db import models


class Product4(models.Model):
    user = models.CharField(max_length=100)
    product = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        app_label = 'database_4'

    def __str__(self):
        return self.product

