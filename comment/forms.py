from django import forms
from .models import Comment, ReplyComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل', 'class':'form-control'}),
            'body': forms.Textarea(attrs={'placeholder': 'نظر شما', 'class': 'form-control'}),
        }


class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model = ReplyComment
        fields = ['name', 'email', 'reply_body']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'reply_body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'نظر شما'})
        }
