from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField (max_length=250)
    content = models.TextField(max_length=600)
    posted_date = models.DateTimeField(auto_now= True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:article_detail', kwargs={'pk': self.pk})
