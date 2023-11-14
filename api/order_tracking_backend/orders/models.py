from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = (
        ('ORDER_CONFIRMED', 'Order Confirmed'),
        ('ORDER_PROCESSING', 'Order Processing'),
        ('SHIPPED', 'Shipped'),
        ('IN_TRANSIT', 'In Transit'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
    )

    order_id = models.CharField(max_length=50, unique=True)
    pin = models.CharField(max_length=4)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ORDER_CONFIRMED')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add other fields like tracking information, date, etc.

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"
