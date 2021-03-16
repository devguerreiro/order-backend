from django.db import models


class Order(models.Model):
    client = models.ForeignKey(
        "core.Client",
        related_name="orders",
        related_query_name="order",
        on_delete=models.CASCADE,
    )
    items = models.ManyToManyField(
        "core.Product",
        related_name="orders",
        related_query_name="order",
        through="core.OrderItem",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.client}"


class OrderItem(models.Model):
    item = models.ForeignKey("core.Product", on_delete=models.CASCADE)
    order = models.ForeignKey("core.Order", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.item}"
