import datetime, os
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from PIL import Image

from CoreApp.manager import UserManager


def photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    date = datetime.datetime.now()
    return f'profile_pics/{instance.username}/{date}-{username}{file_extension}'

def blog_photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    date = datetime.datetime.now()
    return f'blog_pics/{instance.user.username}/{date}-{instance.title}{file_extension}'


class User(AbstractBaseUser, PermissionsMixin):
    email                   = models.EmailField(max_length=255, unique=True)
    username                = models.CharField(max_length=255, unique=True)
    first_name              = models.CharField(max_length=50, null=True)
    last_name               = models.CharField(max_length=50, null=True)
    is_owner                = models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False)
    image                   = models.ImageField(default='ProPic.png', upload_to=photo_path)
    timestamp               = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()

    USERNAME_FIELD          = 'email'
    REQUIRED_FIELDS         = ['username']

    def __str__(self):
        return self.username


class ProfilePics(models.Model):
    user                    = models.ManyToManyField(User, related_name='profile_pics' )
    image                   = models.ImageField(default='ProPic.png', upload_to=photo_path)
    is_approved             = models.BooleanField(default=False)
    timestamp               = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image

    def save(self, *args, **kwargs):
        super(ProfilePics, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


AppUser = get_user_model()
class BlogTopic(models.Model):
    topic                   = models.CharField(max_length=50)
    description             = models.TextField(max_length=150)
    created_by               = models.ForeignKey(AppUser, 
                                on_delete = models.SET_NULL, 
                                related_name= 'blog_topic_creator',
                                blank=True, null=True)
    updated_by              = models.ForeignKey(AppUser, 
                                on_delete = models.SET_NULL,
                                related_name= 'blog_topic_editor',
                                blank=True, null=True)
    created_on              = models.DateTimeField(auto_now_add=True)
    updated_on              = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.topic


class Blog(models.Model):
    user                    = models.ForeignKey(AppUser, 
                                on_delete=models.SET_NULL, 
                                related_name= 'blog_author',
                                null=True)
    title                   = models.CharField(max_length=100, unique=True)
    content                 = models.TextField(max_length=600)
    topic                   = models.ForeignKey(BlogTopic, 
                                on_delete=models.SET_NULL, 
                                related_name= 'blog_topic',
                                blank=True, null=True)
    image                   = models.ImageField( default='blog.png', upload_to=blog_photo_path, blank=True, null=True)
    posted_on               = models.DateTimeField(auto_now_add=True)
    updated_on              = models.DateTimeField()
    approved_by             = models.ForeignKey(AppUser, 
                                on_delete = models.SET_NULL, 
                                related_name= 'blog_approver',
                                blank=True, null=True)
    is_approved             = models.BooleanField(default=False)

    def __str__(self):
        return self.title[:30]
    
    @property
    def author(self):
        return self.user


class Comment(models.Model):
    content                    = models.TextField(max_length=300)
    commented_on            = models.DateTimeField(auto_now_add=True)
    updated_on              = models.DateTimeField(blank=True, null=True)
    user                    = models.ForeignKey(AppUser, 
                                on_delete = models.SET_NULL, 
                                related_name= 'Blog_commenter',
                                blank=True, null=True)
    blog                    = models.ForeignKey(Blog,
                                on_delete = models.CASCADE, 
                                related_name= "commented_blog", 
                                blank=True, null=True)

    def __str__(self):
        return self.content[:10]


class Replay(models.Model):
    text                    = models.TextField(max_length=300)
    replaied_on             = models.DateTimeField(auto_now_add=True)
    updated_on              = models.DateTimeField(blank=True, null=True)
    user                    = models.ForeignKey(AppUser, 
                                on_delete = models.SET_NULL, 
                                related_name= 'commenter_replayer',
                                blank=True, null=True)
    comment                 = models.ForeignKey( Comment, 
                                on_delete = models.SET_NULL, 
                                related_name= 'replayed_comment',
                                blank=True, null=True)

    def __str__(self):
        return self.text[:20]