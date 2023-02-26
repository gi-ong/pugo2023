from django.urls import path
from . import views

app_name = "shorts"

urlpatterns = [
    # path('', views.IndexCreateView.as_view(), name="index"),
    path('',views.index, name="index"),
    path('create', views.create_shorturl, name="create"),
]