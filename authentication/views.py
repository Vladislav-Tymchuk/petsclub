from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.generic import UpdateView
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin



def authenticationView(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.first_name = ""
            form.last_name = ""
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

@login_required
def editView(request, pk):
    if request.user.id != pk:
        return redirect('home')
    if request.method == 'POST':
        customUserForm = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)

        if customUserForm.is_valid():
            customUserForm.save()
            return redirect('home')
    else:
        customUserForm = CustomUserUpdateForm()
    
    return render(request, 'edit.html', {'customUserForm': customUserForm})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change-password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')

def logoutView(request):

	logout(request)
	
	return redirect('home')