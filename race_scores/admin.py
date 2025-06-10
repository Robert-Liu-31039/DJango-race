from django.contrib import admin

# . 代表的是在同一層的物件
from .models import (
    race_scores,
    race_areas,
    race_levels,
    race_years,
    race_colors,
    race_sexs,
    race_finish,
)

# Register your models here.
admin.site.register(race_areas)
admin.site.register(race_levels)
admin.site.register(race_years)
admin.site.register(race_colors)
admin.site.register(race_sexs)
admin.site.register(race_scores)
admin.site.register(race_finish)
