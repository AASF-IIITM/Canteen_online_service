from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import UserForm, UserRegistrationForm


def login_view(request):
    title = "Login"
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        next = request.POST.get("next", 'cafeteria/')
        return HttpResponseRedirect(next)
    return render(request, "registration/login_page.html", {"form": form, "title": title})


def register_view(request):
    title = "Register"
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("menu:detail")

    context = {
        "form": form,
        "title": title,
    }
    return render(request, "registration/login_page.html", context)


def logout_view(request):
    logout(request)
    return redirect("menu:detail")
