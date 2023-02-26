from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Notice(models.Model):
    content = RichTextUploadingField(verbose_name="내용")