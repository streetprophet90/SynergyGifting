from django.db import models
from django.db import models
from gift_platform.users.models import User
from gift_platform.wishlist.models import Item

# Create your models here.


class Order(models.Model):
    giver = models.ForeignKey(User, related_name='giver', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.receiver.username} by {self.giver.username}"
