from django import forms
from .models import Post, Comentario

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('__all__')


class CommentForm(forms.ModelForm):
    contenido = forms.CharField(required=True,widget=forms.Textarea(attrs={
        'rows': 4
    }))
    
    class Meta:
        model = Comentario
        fields = ("contenido",)
