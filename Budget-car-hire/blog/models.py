from django.db import models
from django.conf import settings


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField (max_length=250)
    content = models.TextField(max_length=600)


    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return 
