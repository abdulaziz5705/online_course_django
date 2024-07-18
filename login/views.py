from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'enter/login/login1.html', context={'message': "Password yoki Username xato"})

    return render(request, 'enter/login/login1.html')


def regester_view(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password != password1:
            return render(request, 'enter/regester/registration.html', context={'message_password': " Error Password!!! "})
        else:
            if User.objects.filter(username=username).exists():
                return render(request, 'enter/regester/registration.html', context={'message_username': "Bunday usernamelik foydalanuvchi mavjud "})
            new_user = User(first_name=first_name, last_name=last_name, username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            return redirect('login')
    return render(request, 'enter/regester/registration.html')


def log_out(request):
    logout(request)
    return redirect('index')


def account(request):
    return render(request, 'enter/account.html')




