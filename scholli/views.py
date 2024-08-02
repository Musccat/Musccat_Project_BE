from django.shortcuts import render, redirect

def main(request):
    return render(request, "main.html")

def all_main(request):
    return render(request, "all_main.html")

def index(request):
    #로그인한 경우
    if request.user.is_authenticated:
        return redirect("/main/")
    #로그인하지 않은 경우
    else:
        return redirect("/all_main/")
