from django.db import models
from django.conf import settings
from django.utils.text import slugify
import uuid

class Item(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username + '-' + str(uuid.uuid4()))
        super(Wishlist, self).save(*args, **kwargs)
