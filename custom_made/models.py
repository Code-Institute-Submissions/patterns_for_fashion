from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Fabric(models.Model):
    name = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class CustomProduct(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    price_custom = models.DecimalField(max_digits=6, decimal_places=2)
    fabrics = models.ForeignKey('Fabric', null=True, blank=True, on_delete=models.SET_NULL)
    extra_info = models.TextField

    def __str__(self):
        return self.user


class Measurements(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shoulder_width = models.DecimalField(max_digits=6, decimal_places=2)
    chest_width = models.DecimalField(max_digits=6, decimal_places=2)
    bust_height = models.DecimalField(max_digits=6, decimal_places=2)
    bust_length = models.DecimalField(max_digits=6, decimal_places=2)
    hip_circ1 = models.DecimalField(max_digits=6, decimal_places=2)
    hip_circ2 = models.DecimalField(max_digits=6, decimal_places=2)
    back_width = models.DecimalField(max_digits=6, decimal_places=2)
    back_length = models.DecimalField(max_digits=6, decimal_places=2)
    chest_circ = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.user
