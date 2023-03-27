from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = "Email", required=True)

    class Meta:
        model = User
        fields = ("username", "email")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user