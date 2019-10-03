from django.contrib import admin

from . import models

admin.site.register(models.Fleet)
admin.site.register(models.Transaction)
