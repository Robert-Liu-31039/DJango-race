from django.db import models


# Create your models here.
class race_scores(models.Model):
    player_name = models.CharField(max_length=100)

    referee_a_score = models.FloatField(null=False)
    referee_b_score = models.FloatField(null=False)
    referee_c_score = models.FloatField(null=False)
    avg_score = models.FloatField(null=False)

    # 時間型別中，auto_now_add=True 代表自動帶入現在的時間
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # self 代表是要取同個 model 內的物件
        # id 是 table 預設一定會有的欄位
        return f"{self.player_name} - {self.referee_a_score} - {self.referee_b_score} - {self.referee_c_score}"
