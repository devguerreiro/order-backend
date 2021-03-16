from django.db import models


class Product(models.Model):
    class CurrencyChoices(models.TextChoices):
        REAL = "R$"
        DOLAR = "$"
        EURO = "€"

    name = models.CharField(max_length=150)
    currency = models.CharField(
        max_length=5, choices=CurrencyChoices.choices, default=CurrencyChoices.REAL
    )
    price = models.DecimalField(max_digits=9, decimal_places=2)
    multiplier = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} - {self.currency} {self.price}"
