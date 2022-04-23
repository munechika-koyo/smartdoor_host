from django.urls import path
from . import views


app_name = "authenticate_api"

urlpatterns = [
    path("", views.authenticate, name=""),
]
