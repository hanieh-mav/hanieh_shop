from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('body',)

    error_messages = {
        'body': {
            'required': "You must fill this field.",
        },
    }