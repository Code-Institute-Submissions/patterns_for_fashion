from django.db import models


class Fabric(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024)
    image = models.ImageField()

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
