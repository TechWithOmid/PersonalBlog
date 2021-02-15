from django import forms
from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)
