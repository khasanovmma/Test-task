from PIL import Image

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Product


@receiver(post_save, sender=Product)
def create_webp(sender, instance, created, **kwargs):
    path = instance.image.path
    print(print)
    if instance.image.path[-4:] != "webp":
        im = Image.open(path).convert('RGB')
        extention = instance.image.path.rsplit(".",2)[1]
        file_name = path.replace(extention,"webp") 
        im.save(file_name, 'webp')