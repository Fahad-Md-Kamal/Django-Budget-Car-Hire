from config.settings import *

INSTALLED_APPS +=[
    # Third Parties
    'rest_framework',

    # Apps
    'AppUsers.apps.AppusersConfig',
    'CoreApp.apps.CoreappConfig',
]


AUTH_USER_MODEL = 'CoreApp.User'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL   = '/media/'