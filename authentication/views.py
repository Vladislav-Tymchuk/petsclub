from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib import messages


def authenticationView(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'authentication.html', {'form': form})

def loginView(request):
    messageError = ''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error('Имя пользователя или пароль неверны')
                return redirect('login')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def editView(request):
    
    return render(request, 'edit.html')

def logoutView(request):

	logout(request)
	
	return redirect('home')