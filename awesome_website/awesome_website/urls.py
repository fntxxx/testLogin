from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", include("users.urls")),
    path("admin/", admin.site.urls),
]
