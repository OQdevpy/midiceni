from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from apps.accounts.forms import AccountCreationForm


def main(request):
    return render(request, "main.html")


def loginPage(request):
    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]

        # try:
        #     user = User.objects.get(username=username)
        # except:
        #     messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("patient_list")

        # else:
        #     messages.error(request, 'Username OR password is incorrect')

    return render(request, "login.html")


def register(request):
    form = AccountCreationForm()
    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect("login")
    context = {"form": form}
    return render(request, "register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")
