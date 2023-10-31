from django.shortcuts import render, redirect

from .forms import SignUpForm


def index(request):
    return render(request, "core/index.html")


def contact(request):
    return render(request, "core/contact.html")


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {"form": form})
