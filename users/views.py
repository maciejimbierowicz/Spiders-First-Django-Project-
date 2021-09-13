from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} Created. You can now Log In')
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, 'users/register.html', {'form': form})


