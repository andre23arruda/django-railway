from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):


    class Meta:
        model = Article
        options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
        status = forms.ChoiceField(choices=options)
        exclude = ('slug', 'author', )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Title'
                }),
            'post': forms.Textarea(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Content'
                }),
            'subtitle': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Sub-title'
                }),
            'image_url': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Cover Image'
                })
        }
