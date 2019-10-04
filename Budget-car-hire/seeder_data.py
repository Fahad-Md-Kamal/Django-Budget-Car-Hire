#pylint: disable = no-member, unused-variable
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

## Fake generating script

import random
from django.conf import settings
from django.contrib.auth.models import User

from users.models import Profile
from blog.models import Blog, Comment
from vehicle.models import Vehicle

from faker import Faker
from django.contrib.auth.hashers import make_password

from django.shortcuts import get_object_or_404

fakegen = Faker()
def add_user():
    Fake_username       = fakegen.name()
    Fake_password       = make_password("test1234546")
    Fake_email          = fakegen.email()
    Fake_firstname      = fakegen.first_name()
    Fake_lastname       = fakegen.last_name()
    Fake_staff          = False
    user                = User.objects.get_or_create(username= Fake_username, 
                                                    password= Fake_password, 
                                                    email = Fake_email,
                                                    first_name = Fake_firstname,
                                                    last_name = Fake_lastname,
                                                    is_staff = False )[0]
    return user

def add_blog():
    fake_user           = add_user()
    fake_title          = fakegen.sentences(nb=1, ext_word_list=None)
    fake_content        = fakegen.text(max_nb_chars=600, ext_word_list=None)
    fake_topic          = fakegen.pyint(min_value=0, max_value=2, step=1)
    fake_posted_date    = fakegen.past_date(start_date="-30d", tzinfo=None)
    blog                = Blog.objects.get_or_create( author= fake_user,
                                                    title= fake_title, 
                                                    content= fake_content, 
                                                    topic = fake_topic,
                                                    is_approved = True,
                                                    posted_date = fake_posted_date)[0]
    return blog


def add_vehicles():
    fake_owner          = add_user()
    fake_model_name     = fakegen.pyint(min_value=0, max_value=20, step=1)
    fake_model_year     = fakegen.past_date(start_date="-1200d", tzinfo=None)
    fake_reg_no         = fakegen.license_plate()
    fake_vehicle_type   = fakegen.pyint(min_value=0, max_value=3, step=1)
    fake_added_on       = fakegen.past_date(start_date="-15d", tzinfo=None)
    fake_rent           = fakegen.pyint(min_value=2000, max_value=30000, step=1000)
    fake_capacity       = fakegen.pyint(min_value=2, max_value=35, step=1)
    fake_is_freezed     = fakegen.pyint(min_value=0, max_value=1, step=1)
    fake_is_approved    = fakegen.pyint(min_value=0, max_value=1, step=1)
    
    car                 = Vehicle.objects.get_or_create(owner = fake_owner,
                                                        model_name = fake_model_name,
                                                        model_year = fake_model_year,
                                                        reg_no = fake_reg_no,
                                                        vehicle_type = fake_vehicle_type,
                                                        added_on = fake_added_on,
                                                        rent = fake_rent,
                                                        capacity = fake_capacity,
                                                        is_freezed = fake_is_freezed,
                                                        is_approved = fake_is_approved)

    owner_profile       = get_object_or_404(Profile, user = fake_owner)
    owner_profile.user_type = 1
    owner_profile.save()
    
    return car


def create_comment(N=2):
    for post in range(N):
        post                    = add_blog()
        for entry in range(N):
            user                = add_user()
            fake_comment        = fakegen.text(max_nb_chars=256, ext_word_list=None)
            fake_comment_date   = fakegen.past_date(start_date="-30d", tzinfo=None)
            Comment.objects.get_or_create(  user=user, 
                                            blog=post, 
                                            comment=fake_comment, 
                                            comment_date = fake_comment_date)


def populate_data(N=5):

    for entry in range(N):

        ## Raw Data
        user = add_user() 
        add_blog()
        add_vehicles()

        ## Complex Data
        create_comment()




if __name__ == '__main__':

    user = User.objects.get_or_create(username= 'admin', 
                                    password= make_password("admin123"), 
                                    email = 'admin@gmail.com',
                                    first_name = 'Super',
                                    last_name = 'User',
                                    is_staff = True,
                                    is_superuser = True,
                                    is_active = True )



    print("Super User Created")
    print("#############################################################")  
    user = User.objects.get_or_create(username= 'Moderator', 
                                    password= make_password("password123"), 
                                    email = 'moderator@gmail.com',
                                    first_name = 'Staff',
                                    last_name = 'User',
                                    is_staff = True,
                                    is_superuser = False,
                                    is_active = True )

    print("Moderator Created")
    print("#############################################################")


    print("Populating Data... Please Wait.")
    print("#############################################################")
    populate_data(30)
    print("Populating Data... Complete")
    print("#############################################################")
