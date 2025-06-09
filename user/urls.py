from django.contrib import admin
from django.urls import path

from .views import user_login, user_logout

urlpatterns = [
    # 設定 url 路徑 與 要使用的 function， Django 的根目錄預設不用寫
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]
