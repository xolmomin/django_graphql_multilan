from django.db import models
from django.db.models import CASCADE
from django.utils.translation import gettext as _


class Product(models.Model):
    name=models.CharField(_('name'), max_length=255)
    description=models.CharField(_('description'), max_length=512)
    price = models.FloatField(default=0)
    category = models.ForeignKey('apps.Category', CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(_('name'), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
