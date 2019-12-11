from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from CoreApp.manager import UserManager


# def photo_path(instance, filename):
#     basefilename, file_extension= os.path.splitext(filename)
#     username = instance.user.username
#     date = datetime.datetime.now()
#     return f'profile_pics/{instance.user.id}/{date}-{username}{file_extension}'

class User(AbstractBaseUser, PermissionsMixin):
    email                   = models.EmailField(max_length=255, unique=True)
    username                = models.CharField(max_length=255, unique=True)
    image                   = models.ImageField(default='ProPic.py', upload_to='profile')
    is_staff                = models.BooleanField(default=False)
    timestamp               = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()

    USERNAME_FIELD          = 'email'
    REQUIRED_FIELDS         = ['username']


    # def __str__(self):
    #     return self.username

    # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)

    #     img = Image.open(self.image.path)
        
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
