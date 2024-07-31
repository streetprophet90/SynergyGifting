from django.db import models
from users.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
