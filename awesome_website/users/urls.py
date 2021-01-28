from django.conf.urls import include, url
from users.views import dashboard, register
from django.urls import path

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
]
