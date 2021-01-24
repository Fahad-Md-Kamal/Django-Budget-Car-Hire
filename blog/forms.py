from django import forms
from . import models





class comment_form(forms.ModelForm):
    
    class Meta():
        model = models.Comment
        fields = ('comment',)

        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write Comment'})
        }


class blog_form(forms.ModelForm):

    class Meta:
        model = models.Blog
        fields = ('title', 'content', 'topic')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Title'}),
            'content': forms.Textarea (attrs={'class':'form-control', 'placeholder': 'Max 600 words'})
        }

    # def save(self, commit=True):
    #     # blog = self.instance ##  This helps to keep the author
    #     blog_title = self.cleaned_data['title']
    #     blog_content = self.cleaned_data['content']
    #     blog_topic = self.cleaned_data['topic']