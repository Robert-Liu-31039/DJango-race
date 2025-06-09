from django.shortcuts import render, redirect

from .models import race_scores


from .forms import race_scoresForm


# Create your views here.
def race_scores_list(request):
    user = request.user
    scores_list = race_scores.objects.order_by("-created")

    result = {"scores_list": scores_list, "user": user}

    return render(request, "race_scores/scoreslist.html", result)


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

        return redirect("scoreslist")
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

    return redirect("scoreslist")
