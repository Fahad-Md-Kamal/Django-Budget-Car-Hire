from django import forms
from .models import Comment


class comment_form(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ('comment',)

        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write Comment'})
        }