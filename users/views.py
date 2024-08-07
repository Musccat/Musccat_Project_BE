from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm

def login_view(request):
    if request.method=="POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("/main/")
            else: 
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다.")
        context = {"form": form}
        return render(request, "users/login.html", context)
    else:
        form=LoginForm()
        context={"form": form}
        return render(request, "users/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/users/login/")