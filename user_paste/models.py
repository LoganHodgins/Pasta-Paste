from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=20)
    # TODO: add password

class Post(models.Model):
    # TODO: add post url later
    post_title = models.CharField(max_length=20)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_content = models.TextField(max_length=500)
    post_description = models.CharField(max_length=20)
    post_created_date = models.DateField(auto_now=True)
