from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('name'), max_length=255),
        description=models.CharField(_('description'), max_length=512)
    )

    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
