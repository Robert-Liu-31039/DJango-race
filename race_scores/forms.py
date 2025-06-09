from django.forms import ModelForm
from .models import race_scores


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
            "referee_a_score",
            "referee_b_score",
            "referee_c_score",
        ]
