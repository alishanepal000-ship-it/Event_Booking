from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import SignupForm, LoginForm


def signup_view(request):

    if request.user.is_authenticated:
        return redirect("accounts:profile")

    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(
                request,
                user
            )

            messages.success(
                request,
                "Your account has been created successfully!"
            )

            return redirect(
                "accounts:profile"
            )

    else:

        form = SignupForm()

    return render(
        request,
        "accounts/signup.html",
        {
            "form": form
        }
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("accounts:profile")

    if request.method == "POST":

        form = LoginForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(
                request,
                user
            )

            messages.success(
                request,
                f"Welcome back, {user.username}!"
            )

            next_url = request.GET.get("next")

            if next_url:
                return redirect(next_url)

            return redirect(
                "accounts:profile"
            )

    else:

        form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )


@login_required
def profile_view(request):

    return render(
        request,
        "accounts/profile.html"
    )


def logout_view(request):

    if request.method == "POST":

        logout(request)

        messages.success(
            request,
            "You have been logged out successfully."
        )

        return redirect(
            "accounts:login"
        )

    return redirect(
        "accounts:profile"
    )