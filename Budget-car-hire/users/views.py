from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.conf import settings


from . import forms, models, extras

# Registraiton View
def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            
            # Get form data
            username = form.cleaned_data.get('username')
            tp = form.cleaned_data.get('user_type')
            
            # Saves the requested user while creating user profile with the help of signals
            created_user = form.save()

            # set user type to the profile model
            extras.set_user_type(created_user, tp)
            
            messages.success(request, f'Account created as {username}!')
            return redirect('home')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = forms.UserUpdateForm(request.POST, 
                                      instance=request.user)
        p_form = forms.ProfileUpdateForm(request.POST, 
                                         request.FILES, 
                                         instance=request.user.user_profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Accont {username} has been updated successfully.')
            return redirect('profile')
    else:
        u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.user_profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

def user_detail(request, pk):
    template        = 'users/user_info.html'
    requested_user    = get_object_or_404(auth.models.User, pk = pk)
    context  ={
        'requested_user' : requested_user,
    }

    return render(request, template, context)