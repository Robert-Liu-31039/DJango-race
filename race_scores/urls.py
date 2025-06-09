from django.contrib import admin
from django.urls import path

from .views import race_scores_list, score_add, score_edit, score_delete

urlpatterns = [
    # 設定 url 路徑 與 要使用的 function， Django 的根目錄預設不用寫
    path("", race_scores_list, name="scoreslist"),
    path("score_add/", score_add, name="scoreadd"),
    path("score_edit/<int:id>/", score_edit, name="scoreedit"),
    path("score_delete/<int:id>/", score_delete, name="scoredelete"),
]
