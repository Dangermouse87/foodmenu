from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}. Your account was successfully created!')
            return redirect(('food:index'))
    else:
        form = UserCreationForm
    return render(request, 'users/signup.html', {'form':form})
