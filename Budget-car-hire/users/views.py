from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import forms

def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created as {username}! Please, wait for the account approval.')
            return redirect('home')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = forms.UserUpdateForm(request.POST, instance=request.user)
        p_form = forms.ProfileUpdateForm(request.POST, 
                                         request.FILES, 
                                         instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save(force_insert=False)
            p_form.save(force_insert=False)
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Accont {username} has been updated successfully.')
            return redirect('profile')
    else:
        u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
