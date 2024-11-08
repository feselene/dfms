# urls.py
from django.contrib import admin
from django.urls import path
from . import auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/signup/", auth_views.signup_view, name="signup"),
    path("api/login/", auth_views.login_view, name="login"),
]
