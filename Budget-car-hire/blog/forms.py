from django import forms
from . import models





class comment_form(forms.ModelForm):
    
    class Meta():
        model = models.Comment
        fields = ('comment',)

        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write Comment'})
        }


class article_form(forms.ModelForm):

    class Meta():
        model = models.Article
        fields = ('title', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Title'}),
            'content': forms.Textarea (attrs={'class':'form-control', 'placeholder': 'Max 600 words'})
        }