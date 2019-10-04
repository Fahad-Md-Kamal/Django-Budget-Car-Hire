from django.shortcuts import get_object_or_404

from .models import Profile

def set_user_type(user, type):
    profile = get_object_or_404(Profile, user= user)
    profile.user_type = type
    profile.save()
    return True
