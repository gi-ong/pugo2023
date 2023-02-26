from django.core.validators import URLValidator
from django.db import models

class Short(models.Model):
    full_url = models.URLField(verbose_name="기본URL", validators=[URLValidator])
    short_url = models.CharField(verbose_name="URL 단축값", max_length=30, unique=True)