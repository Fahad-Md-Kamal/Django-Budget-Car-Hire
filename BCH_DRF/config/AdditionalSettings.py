from config.settings import *

INSTALLED_APPS +=[
    # Third Parties

    # Apps
    'AppUsers.apps.AppusersConfig',
    'CoreApp.apps.CoreappConfig',
]

AUTH_USER_MODEL = 'CoreApp.User'