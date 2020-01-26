from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created {username}! ')
            return redirect('home')

    else:
        form = SignUpForm()
        
    return render(request, 'users/signup.html', {'form': form})

