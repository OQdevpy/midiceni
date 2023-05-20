from django.urls import path

from apps.accounts.views import loginPage, logoutUser, main, register

urlpatterns = [
    path("main/", main, name="main"),
    path("", loginPage, name="login"),
    path("register/", register, name="register"),
    path("logout/", logoutUser, name="logout"),
]
