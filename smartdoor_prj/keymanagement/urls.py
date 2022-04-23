from django.urls import path
from . import views


app_name = "keymanagement"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("update/<int:pk>", views.KeyUpdateView.as_view(), name="update_key"),
    path("delete/<int:pk>", views.KeyDeleteView.as_view(), name="delete_key"),
    path("keys/", views.keys, name="keys"),
    path("login/", views.Login.as_view(), name="login"),
    path("registration/", views.RegisterView.as_view(), name="register"),
    path("log/", views.LogView.as_view(), name="log"),
]
