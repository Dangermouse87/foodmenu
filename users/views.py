from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account was successfully created')
            return redirect(('login'))
    else:
        form = UserSignUpForm
    return render(request, 'users/signup.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
