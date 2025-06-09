from django.contrib import admin

# . 代表的是在同一層的物件
from .models import race_scores

# Register your models here.
admin.site.register(race_scores)
