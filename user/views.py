from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def user_login(request):
    message = ""
    username = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username, password)

        user = authenticate(request, username=username, password=password)

        if not user:
            message = "帳號或密碼錯誤!"
        else:
            login(request, user)
            message = "登入成功!"

            # 網頁跳轉至 path name="todolist" 的頁面
            return redirect("raceindex")

    return render(
        request, "user/login.html", {"username": username, "message": message}
    )


def user_logout(request):
    logout(request)
    return redirect("raceindex")
