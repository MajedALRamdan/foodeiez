from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from foodiez import forms
from foodiez import models
# Create your views here.
def home_Page(request):
    categories: list[models.Category] = list(models.Category.objects.all())

    context = {
        "categories": categories,
    }
    return render(request, "home.html", context)
def User_registration(request):
    form = forms.Registerform()
    print(form)
    if request.method == "POST":
        form = forms.Registerform(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.set_password(user. password)
            user.save()
            login(request, user)
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "Register.html", context)

def login_page(request):
    form = forms.UserLogin()
    if request.method == "POST":
        form = forms.UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                print("YES")
                return redirect("home")

    context = {
        "form": form,
    }

    return render(request, "login.html", context)

def logout_page(request):
    logout(request)
    return redirect("home")


def create_category(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("login")
    form = forms.CategoryForm()
    if request.method == "POST":

        form = forms.CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            categor = form.save(commit=False)
            categor.created_by = request.user # assign the created by to the user

            categor.save()
            return redirect("home")

    context = {
        "form": form,
    }
    return render(request, "create_category.html", context)

