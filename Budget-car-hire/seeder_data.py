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
from faker import Faker
from django.contrib.auth.hashers import make_password

fakegen = Faker()

def add_user():
    Fake_username   = fakegen.name();
    Fake_password   = make_password("Test1234546789")
    Fake_email      = fakegen.email()
    Fake_firstname  = fakegen.first_name()
    Fake_lastname   = fakegen.last_name()
    Fake_staff      = False
    user            = User.objects.get_or_create(username= Fake_username, 
                                    password= Fake_password, 
                                    email = Fake_email,
                                    first_name = Fake_firstname,
                                    last_name = Fake_lastname,
                                    is_staff = False )[0]
    return user

def add_blog():
    user = add_user()
    fake_title          = fakegen.sentences(nb=1, ext_word_list=None)
    fake_content        = fakegen.text(max_nb_chars=600, ext_word_list=None)
    fake_topic          = fakegen.pyint(min_value=0, max_value=2, step=1)
    fake_posted_date    = fakegen.past_date(start_date="-30d", tzinfo=None)
    blog = Blog.objects.get_or_create( author= user,
                                title= fake_title, 
                                content= fake_content, 
                                topic = fake_topic,
                                is_approved = True
                                posted_date = fake_posted_date)[0]
    return blog

def create_comment(N=2):
    for post in range(N):
        post                = add_blog()
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
        add_user() 
        add_blog()

        ## Complex Data
        create_comment(N)




if __name__ == '__main__':

    user = User.objects.get_or_create(username= 'Admin', 
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
    populate_data(5)
    print("Populating Data... Complete")