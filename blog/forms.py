from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control bg-light text-dark', 'placeholder': 'نام'}),
            "email": forms.TextInput(attrs={'class': 'form-control bg-light text-dark', 'placeholder': 'ایمیل'}),
            "body": forms.Textarea(attrs={'class': 'form-control bg-light text-dark', 'placeholder': 'متن'})
        }
