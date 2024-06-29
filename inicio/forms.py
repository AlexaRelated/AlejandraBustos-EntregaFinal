from django import forms
from inicio.models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tu nombre'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tu correo electrónico'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Escribe tu comentario aquí'})

        
