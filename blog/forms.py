from django import forms
from django.forms import fields, widgets
from .models import Comment, Post, Categorie

# choices = [('coding','coding'),('hiking','hiking'),('sports','sports')]
choices = Categorie.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title':forms.TextInput(),
            'title_tag':forms.TextInput(),
            'author':forms.TextInput(attrs={'value':'','id':'author','type':'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'required':'required'}),
            'snippet':forms.Textarea(),
            'header_image':forms.FileInput(attrs={'required':'required'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body','snippet', 'header_image')

        widgets = {
            'title':forms.TextInput(),
            'title_tag':forms.TextInput(),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),            
            'body':forms.Textarea(),
            'snippet':forms.Textarea()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        