from django.forms import ModelForm
from .models import (
    race_scores,
    race_areas,
    race_levels,
    race_years,
    race_colors,
    race_sexs,
)


class race_scoresForm(ModelForm):
    class Meta:
        # 宣告 form 使用的是哪個 model
        model = race_scores

        # fields 代表要使用的欄位有哪些
        ## "__all__" 代表 table 所有的欄位都要
        ##fields = "__all__"

        # 指定 要的欄位有哪些
        fields = [
            "player_name",
            "area",
            "level",
            "year",
            "color",
            "sex",
            "referee_a_score",
            "referee_b_score",
            "referee_c_score",
        ]


class race_areasForm(ModelForm):
    class Meta:
        # 宣告 form 使用的是哪個 model
        model = race_areas

        # fields 代表要使用的欄位有哪些
        ## "__all__" 代表 table 所有的欄位都要
        ##fields = "__all__"

        # 指定 要的欄位有哪些
        fields = [
            "id",
            "area",
        ]


class race_levelsForm(ModelForm):
    class Meta:
        # 宣告 form 使用的是哪個 model
        model = race_levels

        # fields 代表要使用的欄位有哪些
        ## "__all__" 代表 table 所有的欄位都要
        ##fields = "__all__"

        # 指定 要的欄位有哪些
        fields = [
            "id",
            "level",
        ]


class race_yearsForm(ModelForm):
    class Meta:
        # 宣告 form 使用的是哪個 model
        model = race_years

        # fields 代表要使用的欄位有哪些
        ## "__all__" 代表 table 所有的欄位都要
        ##fields = "__all__"

        # 指定 要的欄位有哪些
        fields = [
            "id",
            "year",
        ]


class race_colorsForm(ModelForm):
    class Meta:
        # 宣告 form 使用的是哪個 model
        model = race_colors

        # fields 代表要使用的欄位有哪些
        ## "__all__" 代表 table 所有的欄位都要
        ##fields = "__all__"

        # 指定 要的欄位有哪些
        fields = [
            "id",
            "color",
        ]


class race_sexsForm(ModelForm):
    class Meta:
        # 宣告 form 使用的是哪個 model
        model = race_sexs

        # fields 代表要使用的欄位有哪些
        ## "__all__" 代表 table 所有的欄位都要
        ##fields = "__all__"

        # 指定 要的欄位有哪些
        fields = [
            "id",
            "sex",
        ]
