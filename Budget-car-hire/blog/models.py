from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

class Blog(models.Model):
    OT = 0
    VH = 1
    SV = 2
    blog_TOPICS = [
        (OT, 'Others'),
        (VH, 'Vehicle'),
        (SV, 'Service'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField (max_length=250)
    content = models.TextField(max_length=600)
    topic = models.IntegerField(choices=blog_TOPICS, default=OT)
    posted_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    @staticmethod
    def approve(self):
        self.is_approved = not self.is_approved
        self.save()
        
        
    def get_absolute_url(self):
        return reverse('blogs:blog_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-posted_date',]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="user_comment")
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name="comments")
    comment = models.TextField(max_length= 256)
    comment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('blogs:blog_detail', kwargs={'pk': self.blog.pk})

    class Meta:
        ordering = ['-comment_date',]