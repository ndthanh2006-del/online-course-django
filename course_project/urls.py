from django.contrib import admin
from django.urls import include, path
from onlinecourse import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("courses/", include("onlinecourse.urls")),
]
