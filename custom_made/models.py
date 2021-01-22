from django.db import models
from django.contrib.auth.models import User

from products.models import Product

# Create your models here.


class CustomProduct(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    price_custom = models.DecimalField(Product, max_digits=6, decimal_places=2)
    shoulder_width = models.DecimalField(max_digits=6, decimal_places=2)
    chest_width = models.DecimalField(max_digits=6, decimal_places=2)
    bust_height = models.DecimalField(max_digits=6, decimal_places=2)
    bust_length = models.DecimalField(max_digits=6, decimal_places=2)
    hip_circ1 = models.DecimalField(max_digits=6, decimal_places=2)
    hip_circ2 = models.DecimalField(max_digits=6, decimal_places=2)
    back_width = models.DecimalField(max_digits=6, decimal_places=2)
    back_length = models.DecimalField(max_digits=6, decimal_places=2)
    chest_circ = models.DecimalField(max_digits=6, decimal_places=2)
    extra_info = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username
