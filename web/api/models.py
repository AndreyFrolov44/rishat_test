from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Discount(models.Model):
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.discount_amount)


class Tax(models.Model):
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.tax_amount)


class Order(models.Model):
    items = models.ManyToManyField(Item)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, blank=True, null=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, blank=True, null=True)
