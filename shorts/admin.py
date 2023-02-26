from django.contrib import admin
from . import models

@admin.register(models.Short)
class ShortsAdmin(admin.ModelAdmin):
    list_display = (
        "full_url",
        "short_url"
    )