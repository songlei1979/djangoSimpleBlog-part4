from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('id', 'name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'auther', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'auther': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'userinput', 'type':'hidden'}),
            # 'auther': forms.Select(attrs={'class': 'form-control'}),
            # 'category': forms.Select(choices = choices, attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag',  'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }