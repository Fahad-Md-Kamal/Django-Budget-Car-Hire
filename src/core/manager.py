from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Manages Users or Superusers
    """
    def create_user(self, email, username, password=None):
        """
        Create a new user profile
        """
        if not email:
            raise ValueError('User must have a email address')

        email = self.normalize_email(email)
        user = self.model(email = email, username = username)

        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, email, password, username):
        """
        Create superuser for user app
        """
        user = self.create_user(email, username, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
