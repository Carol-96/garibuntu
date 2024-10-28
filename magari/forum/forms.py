from django import forms
from .models import ForumThread, ForumPost, ForumReply

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