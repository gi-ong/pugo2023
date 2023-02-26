from django.shortcuts import render
from django.views.generic import DetailView
from . import models

class NoticeDetailView(DetailView):
    model = models.Notice
    template_name = "notice_detail.html"

