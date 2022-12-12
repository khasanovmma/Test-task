from django.db import models


class CreatedAbstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedAbstract(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CreatedUpdatedAtAbstract(CreatedAbstract, UpdatedAbstract):
    class Meta:
        abstract = True
        ordering = ["-created_at"]
