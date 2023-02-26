from django.urls import path
from . import views

app_name = "boards"

urlpatterns = [
    path('<int:pk>',views.NoticeDetailView.as_view(), name="detail"),
]