from django.contrib import admin

from CoreApp import models

admin.site.register(models.User)
admin.site.register(models.BlogTopic)
admin.site.register(models.Blog)
admin.site.register(models.Comment)
admin.site.register(models.Replay)
