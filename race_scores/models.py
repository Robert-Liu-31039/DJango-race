from django.db import models


# Create your models here.
class race_areas(models.Model):
    area = models.CharField(max_length=50)

    def __str__(self):  # self 代表是要取同個 model 內的物件
        # id 是 table 預設一定會有的欄位
        return f"{self.id} - {self.area}"


class race_levels(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):  # self 代表是要取同個 model 內的物件
        # id 是 table 預設一定會有的欄位
        return f"{self.id} - {self.level}"


class race_years(models.Model):
    year = models.CharField(max_length=50)

    def __str__(self):  # self 代表是要取同個 model 內的物件
        # id 是 table 預設一定會有的欄位
        return f"{self.id} - {self.year}"


class race_colors(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):  # self 代表是要取同個 model 內的物件
        # id 是 table 預設一定會有的欄位
        return f"{self.id} - {self.color}"


class race_sexs(models.Model):
    sex = models.CharField(max_length=50)

    def __str__(self):  # self 代表是要取同個 model 內的物件
        # id 是 table 預設一定會有的欄位
        return f"{self.id} - {self.sex}"


class race_scores(models.Model):
    player_name = models.CharField(max_length=100)
    area = models.ForeignKey(race_areas, on_delete=models.CASCADE)
    level = models.ForeignKey(race_levels, on_delete=models.CASCADE)
    year = models.ForeignKey(race_years, on_delete=models.CASCADE)
    color = models.ForeignKey(race_colors, on_delete=models.CASCADE)
    sex = models.ForeignKey(race_sexs, on_delete=models.CASCADE)

    referee_a_score = models.FloatField(null=True, blank=True)
    referee_b_score = models.FloatField(null=True, blank=True)
    referee_c_score = models.FloatField(null=True, blank=True)
    avg_score = models.FloatField(null=True, blank=True)
    projection_tag = models.BooleanField(default=False)

    score_update = models.DateTimeField(null=True, blank=True)

    # 時間型別中，auto_now_add=True 代表自動帶入現在的時間
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # self 代表是要取同個 model 內的物件
        # id 是 table 預設一定會有的欄位
        return f"{self.player_name} - {self.referee_a_score} - {self.referee_b_score} - {self.referee_c_score}"


class race_finish(models.Model):
    area = models.ForeignKey(race_areas, on_delete=models.CASCADE)
    level = models.ForeignKey(race_levels, on_delete=models.CASCADE)
    year = models.ForeignKey(race_years, on_delete=models.CASCADE)
    color = models.ForeignKey(race_colors, on_delete=models.CASCADE)
    sex = models.ForeignKey(race_sexs, on_delete=models.CASCADE)

    # 時間型別中，auto_now_add=True 代表自動帶入現在的時間
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # self 代表是要取同個 model 內的物件
        # id 是 table 預設一定會有的欄位
        return f"{self.area} - {self.level} - {self.year} - {self.color} - {self.sex}"


class team_demo_levels(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):  # self 代表是要取同個 model 內的物件
        # id 是 table 預設一定會有的欄位
        return f"{self.id} - {self.level}"


class team_demo_scores(models.Model):
    player_name = models.CharField(max_length=100)
    level = models.ForeignKey(team_demo_levels, on_delete=models.CASCADE)

    referee_a_score = models.FloatField(null=True, blank=True)
    referee_b_score = models.FloatField(null=True, blank=True)
    referee_c_score = models.FloatField(null=True, blank=True)
    referee_d_score = models.FloatField(null=True, blank=True)
    referee_e_score = models.FloatField(null=True, blank=True)
    sum_score = models.FloatField(null=True, blank=True)
    projection_tag = models.BooleanField(default=False)

    score_update = models.DateTimeField(null=True, blank=True)

    # 時間型別中，auto_now_add=True 代表自動帶入現在的時間
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # self 代表是要取同個 model 內的物件
        # id 是 table 預設一定會有的欄位
        return f"{self.player_name} - {self.referee_a_score} - {self.referee_b_score} - {self.referee_c_score} - {self.referee_d_score} - {self.referee_e_score}"


class team_demo_finish(models.Model):
    level = models.ForeignKey(team_demo_levels, on_delete=models.CASCADE)

    # 時間型別中，auto_now_add=True 代表自動帶入現在的時間
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # self 代表是要取同個 model 內的物件
        # id 是 table 預設一定會有的欄位
        return f"{self.level}"
