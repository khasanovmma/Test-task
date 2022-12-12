from rest_framework import serializers

from apps.store.models import Product 


class ProductSerializer(serializers.ModelSerializer):
    image =  serializers.SerializerMethodField(method_name="get_image")

    def get_image(self, product: Product):
        image_format = ''
        return {
            "path": product.image.url[:-4] if product.image.url[-3:] in ["png", "jpg"] else product.image.url[:-5],
            "formats": [product.image.url[-3:], "webp"] if product.image.url[-3:] in ["png", "jpg"] else ["webp"]
        }

    class Meta:
        model =  Product
        fields = ["id", "title", "description", "status", "image"]
        read_only_fields = fields