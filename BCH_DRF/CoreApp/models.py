import datetime, os, uuid
from django.db import models
from django.db.models.signals import post_save
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

def vehicle_photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    uid  = uuid.uuid4()
    return f'vehicle_pics/{instance.registration_no}/{uid}-{instance.registration_no}{file_extension}'


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
    image                   = models.ImageField(default='ProPic.png', 
                                upload_to=photo_path)
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
    image                   = models.ImageField( default='blog.png', 
                                upload_to=blog_photo_path, 
                                blank=True, null=True)
    posted_on               = models.DateTimeField(auto_now_add=True)
    updated_on              = models.DateTimeField(blank=True, null=True)
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
    text                    = models.TextField(max_length=300)
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
    parent_comment          = models.ForeignKey( 'self', 
                                on_delete = models.SET_NULL,
                                blank=True, null=True)

    def __str__(self):
        return self.text[:30]


class VehicleCategory(models.Model):
    name                    = models.CharField(max_length=20, unique=True)
    description             = models.TextField(max_length=100)
    created_on              = models.DateTimeField(auto_now_add=True)
    created_by              = models.ForeignKey(AppUser, 
                                on_delete= models.SET_NULL, 
                                related_name= 'category_creator',
                                blank=True, null=True)
    updated_on              = models.DateTimeField(auto_now_add=True)
    updated_by              = models.ForeignKey(AppUser, 
                                on_delete= models.SET_NULL, 
                                related_name= 'category_updator',
                                blank=True, null=True)

    def __str__(self):
        return self.name


class VehicleModel(models.Model):
    name                    = models.CharField(max_length=20, unique=True)
    description             = models.TextField(max_length=100)
    created_on              = models.DateTimeField(auto_now_add=True)
    created_by              = models.ForeignKey(AppUser, 
                                on_delete= models.SET_NULL, 
                                related_name= 'model_creator',
                                blank=True, null=True)
    updated_on              = models.DateTimeField(auto_now_add=True)
    updated_by              = models.ForeignKey(AppUser, 
                                on_delete= models.SET_NULL, 
                                related_name= 'model_updator',
                                blank=True, null=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    registration_no         = models.CharField(max_length=20, unique=True)
    registared_on           = models.DateTimeField(auto_now_add=True)
    rent                    = models.PositiveIntegerField(default = 2000)
    capacity                = models.PositiveIntegerField(default = 2)
    is_blocked              = models.BooleanField(default=False)
    is_approved             = models.BooleanField(default=False)
    is_booked               = models.BooleanField(default=False)
    is_hired                = models.BooleanField(default=False)
    booked_date             = models.DateTimeField(blank=True, null=True)
    user                    = models.ForeignKey(AppUser, 
                                on_delete = models.SET_NULL, 
                                related_name= 'vehicle_owner',
                                blank=True, null=True)
    model                   = models.ForeignKey(VehicleModel, 
                                on_delete = models.SET_NULL, 
                                related_name= 'vehicle_model',
                                blank=True, null=True)
    category                = models.ForeignKey(VehicleCategory, 
                                on_delete = models.SET_NULL, 
                                related_name= 'vehicle_category',
                                blank=True, null=True)

    @property
    def owner(self):
        return self.user
    
    def __str__(self):
        return self.registration_no 


class VehiclePics(models.Model):
    vehicle                 = models.ForeignKey(Vehicle, 
                                related_name='vehicle_pics', 
                                on_delete = models.SET_DEFAULT, 
                                default = 1 )
    image                   = models.ImageField(default='ProPic.png', 
                                upload_to=photo_path)
    is_approved             = models.BooleanField(default=False)
    timestamp               = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle.registration_no + " - Picture"

    def save(self, *args, **kwargs):
        super(VehiclePics, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 600:
            output_size = (400, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)

