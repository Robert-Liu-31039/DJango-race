from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
import pandas as pd
from django.http import HttpResponse
from django.db import connection
from io import BytesIO

from .models import (
    race_scores,
    race_areas,
    race_levels,
    race_years,
    race_colors,
    race_sexs,
    race_finish,
    team_demo_levels,
    team_demo_scores,
    team_demo_finish,
)


from .forms import (
    race_scoresForm,
    race_areasForm,
    race_levelsForm,
    race_yearsForm,
    race_colorsForm,
    race_sexsForm,
    team_demo_levelsForm,
    team_demo_scoresForm,
)

from datetime import datetime


# Create your views here.
def race_areas_list(request):
    areas_list = race_areas.objects.all()

    if request.method == "POST":
        # 將 原本 form 的內容記憶起來，用於執行 Insert
        form = race_areasForm(request.POST)

        # 暫存，不做 commit，因為還有資料要做處理
        area = form.save(commit=False)

        # 真的存於 db 中
        area.save()

        return redirect("areaslist")
    else:
        form = race_areasForm

    return render(
        request, "race_scores/editarea.html", {"datas": areas_list, "form": form}
    )


def area_delete(request, id):  # Django 規定 : 一定要帶 request 這個參數
    area = race_areas.objects.get(id=id)
    area.delete()

    return redirect("areaslist")


def race_levels_list(request):
    levels_list = race_levels.objects.all()

    if request.method == "POST":
        # 將 原本 form 的內容記憶起來，用於執行 Insert
        form = race_levelsForm(request.POST)

        # 暫存，不做 commit，因為還有資料要做處理
        level = form.save(commit=False)

        # 真的存於 db 中
        level.save()

        return redirect("levelslist")
    else:
        form = race_levelsForm

    return render(
        request, "race_scores/editlevel.html", {"datas": levels_list, "form": form}
    )


def level_delete(request, id):  # Django 規定 : 一定要帶 request 這個參數
    level = race_levels.objects.get(id=id)
    level.delete()

    return redirect("levelslist")


def race_years_list(request):
    years_list = race_years.objects.all()

    if request.method == "POST":
        # 將 原本 form 的內容記憶起來，用於執行 Insert
        form = race_yearsForm(request.POST)

        # 暫存，不做 commit，因為還有資料要做處理
        year = form.save(commit=False)

        # 真的存於 db 中
        year.save()

        return redirect("yearslist")
    else:
        form = race_yearsForm

    return render(
        request, "race_scores/edityear.html", {"datas": years_list, "form": form}
    )


def year_delete(request, id):  # Django 規定 : 一定要帶 request 這個參數
    year = race_years.objects.get(id=id)
    year.delete()

    return redirect("yearslist")


def race_colors_list(request):
    colors_list = race_colors.objects.all()

    if request.method == "POST":
        # 將 原本 form 的內容記憶起來，用於執行 Insert
        form = race_colorsForm(request.POST)

        # 暫存，不做 commit，因為還有資料要做處理
        color = form.save(commit=False)

        # 真的存於 db 中
        color.save()

        return redirect("colorslist")
    else:
        form = race_colorsForm

    return render(
        request, "race_scores/editcolor.html", {"datas": colors_list, "form": form}
    )


def color_delete(request, id):  # Django 規定 : 一定要帶 request 這個參數
    color = race_colors.objects.get(id=id)
    color.delete()

    return redirect("colorslist")


def race_sexs_list(request):
    sexs_list = race_sexs.objects.all()

    if request.method == "POST":
        # 將 原本 form 的內容記憶起來，用於執行 Insert
        form = race_sexsForm(request.POST)

        # 暫存，不做 commit，因為還有資料要做處理
        sex = form.save(commit=False)

        # 真的存於 db 中
        sex.save()

        return redirect("sexslist")
    else:
        form = race_sexsForm

    return render(
        request, "race_scores/editsex.html", {"datas": sexs_list, "form": form}
    )


def sex_delete(request, id):  # Django 規定 : 一定要帶 request 這個參數
    sex = race_sexs.objects.get(id=id)
    sex.delete()

    return redirect("sexslist")


def race_list(request):
    race_list = race_scores.objects.all()

    if request.method == "POST":

        # 將 原本 form 的內容記憶起來，用於執行 Insert
        form = race_scoresForm(request.POST)

        # 暫存，不做 commit，因為還有資料要做處理
        form = form.save(commit=False)

        # 真的存於 db 中
        form.save()

        return redirect("raceslist")
    else:
        form = race_scoresForm

    return render(
        request, "race_scores/editrace.html", {"datas": race_list, "form": form}
    )


def race_delete(request, id):  # Django 規定 : 一定要帶 request 這個參數
    race = race_scores.objects.get(id=id)
    race.delete()

    return redirect("raceslist")


def race_index(request):
    user = request.user
    scores_list = race_scores.objects.order_by("-created")
    area_list = race_areas.objects.order_by("area")

    result = {"scores_list": scores_list, "area_list": area_list, "user": user}

    return render(request, "race_scores/raceindex.html", result)


def race_start(request, id):
    user = request.user
    area_list = race_areas.objects.filter(id=id).first()
    race_list = None

    finish_tag = None
    if request.method == "POST":
        race_list = race_scores.objects.filter(area_id=id).order_by("-created")

        if request.POST.get("level"):
            race_list = race_list.filter(level_id=request.POST.get("level"))

        if request.POST.get("year"):
            race_list = race_list.filter(year_id=request.POST.get("year"))

        if request.POST.get("color"):
            race_list = race_list.filter(color_id=request.POST.get("color"))

        if request.POST.get("sex"):
            race_list = race_list.filter(sex_id=request.POST.get("sex"))

        form = race_scoresForm(request.POST)

        for data in race_list.all():
            if data.projection_tag:
                finish_tag = "Y"
    else:
        form = race_scoresForm

    result = {
        "datas": race_list,
        "area_list": area_list,
        "user": user,
        "finish_tag": finish_tag,
        "form": form,
    }

    return render(request, "race_scores/racestart.html", result)


def change_projection(request):

    id = request.GET.get("pt")
    area_id = request.GET.get("ad")

    result = None
    success = False

    try:
        # 移除比賽結束的紀錄
        old = race_finish.objects.filter(area_id=area_id)
        if old:
            old.delete()

        race_scores.objects.filter(area_id=area_id).update(projection_tag=False)

        updateProjectionTag = get_object_or_404(race_scores, id=id)
        updateProjectionTag.projection_tag = True

        updateProjectionTag.save()

        result = "投影成功"
        success = True
    except Exception as ex:
        result = "投影失敗" + ex

    return JsonResponse({"success": success, "result": result})


def cancel_projection(request, id):
    race_scores.objects.filter(area_id=id).update(projection_tag=False)

    return redirect(reverse("racestart", kwargs={"id": id}))


def update_score(request):
    id = request.GET.get("pt")
    referee_a_score = request.GET.get("a")
    referee_b_score = request.GET.get("b")
    referee_c_score = request.GET.get("c")

    result = None
    success = False

    try:
        updateScore = get_object_or_404(race_scores, id=id)
        updateScore.referee_a_score = referee_a_score
        updateScore.referee_b_score = referee_b_score
        updateScore.referee_c_score = referee_c_score
        updateScore.avg_score = (
            float(
                float(referee_a_score) + float(referee_b_score) + float(referee_c_score)
            )
            / 3
        )

        updateScore.score_update = datetime.now()

        updateScore.save()

        result = "分數更新成功"
        success = True
    except Exception as ex:
        result = "分數更新失敗" + ex

    return JsonResponse({"success": success, "result": result})


def print_projection(request, id):
    user = request.user
    area_list = race_areas.objects.filter(id=id).first()
    datas = race_scores.objects.filter(area_id=id, projection_tag=True).all()

    finish_datas = None
    finish_game = race_finish.objects.filter(area_id=id).first()
    if finish_game:
        finish_datas = (
            race_scores.objects.filter(
                area_id=finish_game.area_id,
                level_id=finish_game.level_id,
                year_id=finish_game.year_id,
                color_id=finish_game.color_id,
                sex_id=finish_game.sex_id,
            )
            .order_by("-avg_score")
            .all()
        )

    result = {
        "datas": datas,
        "finish_datas": finish_datas,
        "area_list": area_list,
        "user": user,
    }

    return render(request, "race_scores/printprojection.html", result)


def finish_game(request, id):
    user = request.user

    # 移除舊的比賽結束的紀錄
    old = race_finish.objects.filter(area_id=id)
    if old:
        old.delete()

    last_data = race_scores.objects.filter(area_id=id).order_by("-score_update").first()

    if last_data:
        insert_datas = []
        insert_datas.append(
            race_finish(
                area_id=last_data.area_id,
                level_id=last_data.level_id,
                year_id=last_data.year_id,
                color_id=last_data.color_id,
                sex_id=last_data.sex_id,
            )
        )

        race_finish.objects.bulk_create(insert_datas, ignore_conflicts=True)

    # 移除投影的設定
    race_scores.objects.filter(area_id=id).update(projection_tag=False)

    return redirect(reverse("racestart", kwargs={"id": id}))


def export_race_scores_to_csv(request):
    # 使用 raw SQL 查詢資料
    query = "SELECT id,player_name,referee_a_score,referee_b_score,referee_c_score,avg_score FROM race_scores_race_scores"
    df1 = pd.read_sql(query, connection)

    query2 = "SELECT id,player_name,referee_a_score,referee_b_score,referee_c_score,referee_d_score,referee_e_score,sum_score FROM race_scores_team_demo_scores"
    df2 = pd.read_sql(query2, connection)

    # 建立 Excel 檔案的記憶體緩衝區
    output = BytesIO()

    # 用 ExcelWriter 把多個 Sheet 寫入同一個檔案中
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df1.to_excel(writer, sheet_name="race_scores_data", index=False)
        df2.to_excel(writer, sheet_name="team_demo_scores_data", index=False)

    # 將檔案指標移至開頭
    output.seek(0)

    # 傳回給使用者下載
    response = HttpResponse(
        output,
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = 'attachment; filename="data.xlsx"'

    return response


def team_demo_levels_list(request):
    levels_list = team_demo_levels.objects.all()

    if request.method == "POST":
        # 將 原本 form 的內容記憶起來，用於執行 Insert
        form = team_demo_levelsForm(request.POST)

        # 暫存，不做 commit，因為還有資料要做處理
        level = form.save(commit=False)

        # 真的存於 db 中
        level.save()

        return redirect("teamdemolevelslist")
    else:
        form = team_demo_levelsForm

    return render(
        request,
        "race_scores/teamdemoeditlevel.html",
        {"datas": levels_list, "form": form},
    )


def team_demo_level_delete(request, id):  # Django 規定 : 一定要帶 request 這個參數
    level = team_demo_levels.objects.get(id=id)
    level.delete()

    return redirect("teamdemolevelslist")


def team_demo_race_list(request):
    race_list = team_demo_scores.objects.all()

    if request.method == "POST":

        # 將 原本 form 的內容記憶起來，用於執行 Insert
        form = team_demo_scoresForm(request.POST)

        # 暫存，不做 commit，因為還有資料要做處理
        form = form.save(commit=False)

        # 真的存於 db 中
        form.save()

        return redirect("teamdemoraceslist")
    else:
        form = team_demo_scoresForm

    return render(
        request, "race_scores/teamdemoeditrace.html", {"datas": race_list, "form": form}
    )


def team_demo_race_delete(request, id):  # Django 規定 : 一定要帶 request 這個參數
    race = team_demo_scores.objects.get(id=id)
    race.delete()

    return redirect("teamdemoraceslist")


def team_demo_race_start(request):
    user = request.user
    race_list = None

    finish_tag = None
    if request.method == "POST":
        race_list = team_demo_scores.objects.order_by("-created")

        if request.POST.get("level"):
            race_list = race_list.filter(level=request.POST.get("level"))

        form = team_demo_scoresForm(request.POST)

        for data in race_list.all():
            if data.projection_tag:
                finish_tag = "Y"
    else:
        form = team_demo_scoresForm

    result = {
        "datas": race_list,
        "user": user,
        "finish_tag": finish_tag,
        "form": form,
    }

    return render(request, "race_scores/teamdemoracestart.html", result)


def change_team_demo_projection(request):

    id = request.GET.get("pt")

    result = None
    success = False

    try:
        team_demo_scores.objects.update(projection_tag=False)

        updateProjectionTag = get_object_or_404(team_demo_scores, id=id)
        updateProjectionTag.projection_tag = True

        updateProjectionTag.save()

        # 移除舊的比賽結束的紀錄
        old = team_demo_finish.objects.all()
        if old:
            old.delete()

        result = "投影成功"
        success = True
    except Exception as ex:
        result = "投影失敗" + ex

    return JsonResponse({"success": success, "result": result})


def cancel_team_demo_projection(request):
    datas = team_demo_scores.objects.filter(projection_tag=True).all()

    level_id = None
    if datas:
        level_id = datas[0].level

    team_demo_scores.objects.filter(level_id=level_id).update(projection_tag=False)

    return redirect(reverse("teamdemoracestart"))


def update_team_demo_score(request):
    id = request.GET.get("pt")
    referee_a_score = request.GET.get("a")
    referee_b_score = request.GET.get("b")
    referee_c_score = request.GET.get("c")
    referee_d_score = request.GET.get("d")
    referee_e_score = request.GET.get("e")

    result = None
    success = False

    try:
        updateScore = get_object_or_404(team_demo_scores, id=id)
        updateScore.referee_a_score = referee_a_score
        updateScore.referee_b_score = referee_b_score
        updateScore.referee_c_score = referee_c_score
        updateScore.referee_d_score = referee_d_score
        updateScore.referee_e_score = referee_e_score
        updateScore.sum_score = float(
            float(referee_a_score)
            + float(referee_b_score)
            + float(referee_c_score)
            + float(referee_d_score)
            + float(referee_e_score)
        )

        updateScore.score_update = datetime.now()

        updateScore.save()

        result = "分數更新成功"
        success = True
    except Exception as ex:
        result = "分數更新失敗" + ex

    return JsonResponse({"success": success, "result": result})


def print_team_demo_projection(request):
    user = request.user
    datas = team_demo_scores.objects.filter(projection_tag=True).all()

    level_id = None
    if datas:
        level_id = datas[0].level

    finish_datas = None
    finish_game = team_demo_finish.objects.first()
    if finish_game:
        finish_datas = (
            team_demo_scores.objects.filter(
                level_id=finish_game.level_id,
            )
            .order_by("-sum_score")
            .all()
        )

    result = {
        "datas": datas,
        "finish_datas": finish_datas,
        "user": user,
    }

    return render(request, "race_scores/printteamdemoprojection.html", result)


def finish_team_demo_game(request):
    user = request.user

    datas = team_demo_scores.objects.filter(projection_tag=True).all()

    level_id = None
    if datas:
        level_id = datas[0].level

    # 移除舊的比賽結束的紀錄
    old = team_demo_finish.objects.filter(level_id=level_id)
    if old:
        old.delete()

    last_data = (
        team_demo_scores.objects.filter(level_id=level_id)
        .order_by("-score_update")
        .first()
    )

    if last_data:
        insert_datas = []
        insert_datas.append(
            race_finish(
                level_id=last_data.level_id,
            )
        )

        team_demo_finish.objects.bulk_create(insert_datas, ignore_conflicts=True)

    # 移除投影的設定
    team_demo_scores.objects.filter(level_id=level_id).update(projection_tag=False)

    return redirect(reverse("teamdemoracestart"))


def score_add(request):
    if request.method == "POST":
        # 將 原本 form 的內容記憶起來，用於執行 Insert
        form = race_scoresForm(request.POST)

        # 暫存，不做 commit，因為還有資料要做處理
        score = form.save(commit=False)
        score.avg_score = (
            float(score.referee_a_score + score.referee_b_score + score.referee_c_score)
            / 3
        )

        # 真的存於 db 中
        score.save()

        return redirect("raceindex")
    else:
        form = race_scoresForm

    return render(request, "race_scores/createscore.html", {"form": form})


def score_edit(request, id):  # Django 規定 : 一定要帶 request 這個參數
    score = None
    form = None
    message = None

    try:
        score = race_scores.objects.get(id=id)

        if request.method == "GET":
            # instance -> 實際案例，代表要放在 TodoForm 的資料實例
            form = race_scoresForm(instance=score)
        else:
            # 將 原本 form 的內容記憶起來，並取代 原本instance 的資料，用於執行 Update
            form = race_scoresForm(request.POST, instance=score)

            # 暫存，不做 commit，因為還有資料要做處理
            action = form.save(commit=False)
            action.avg_score = (
                float(
                    score.referee_a_score
                    + score.referee_b_score
                    + score.referee_c_score
                )
                / 3
            )

            # 真的存於 db 中
            action.save()

            message = "修改成功"

    except Exception as e:
        print(e)

    return render(
        request,
        "race_scores/editscore.html",
        {"score": score, "form": form, "message": message},
    )


def score_delete(request, id):  # Django 規定 : 一定要帶 request 這個參數
    score = race_scores.objects.get(id=id)
    score.delete()

    return redirect("raceindex")
