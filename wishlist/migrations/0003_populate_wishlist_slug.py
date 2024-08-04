from django.db import migrations, models
from django.utils.text import slugify
import uuid

def populate_wishlist_slug(apps, schema_editor):
    Wishlist = apps.get_model('wishlist', 'Wishlist')
    for wishlist in Wishlist.objects.all():
        if not wishlist.slug:
            wishlist.slug = slugify(wishlist.user.username + '-' + str(uuid.uuid4()))
            wishlist.save()

class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_wishlist_slug'),
    ]

    operations = [
        migrations.RunPython(populate_wishlist_slug),
    ]
