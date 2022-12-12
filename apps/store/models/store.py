from django.db import models

from apps.core.models import CreatedUpdatedAtAbstract


class Product(CreatedUpdatedAtAbstract):
    class ProductStatus(models.TextChoices):
        IN_STOCK = "in_stock", "В наличии"
        ON_ORDER = "on_order", "Под заказ"
        RECEIPT_EXPECTED = "receipt_expected", "Ожидается поступление"
        NOT_AVAILABLE = "not_available", "Нет в наличии"
        NOT_PRODUCED = "not_produced", "Не производится"

    title = models.CharField(max_length=125)
    description = models.TextField(blank=True, null=True)
    price =  models.PositiveBigIntegerField()
    status = models.CharField(max_length=50, choices=ProductStatus.choices, default=ProductStatus.IN_STOCK)
    image = models.ImageField(upload_to="images/")