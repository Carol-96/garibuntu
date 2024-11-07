from django import forms
from .models import ForumThread, ForumPost, ForumReply
from django import forms
from .models import ForumThread

class ThreadForm(forms.ModelForm):
    class Meta:
        model = ForumThread
        fields = ['title', 'description']

class PostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['content']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = ForumReply
        fields = ['content']


class ForumThreadForm(forms.ModelForm):
    class Meta:
        model = ForumThread
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter thread title', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter thread text', 'class': 'form-control'}),
        }