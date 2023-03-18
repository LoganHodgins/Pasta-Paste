from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['post_author', 'post_created_date', 'post_url_slug']
        labels = {
            'post_title': 'Paste Title',
            'post_content': '',
            'post_description': 'Short Description',
            'post_category': 'Category',
            'post_type': 'Type',
        }
