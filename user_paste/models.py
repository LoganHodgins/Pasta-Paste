from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=20, unique=True)
    user_created_date = models.DateTimeField(auto_now_add=True)
    # TODO: add password

    def __str__(self):
        return f'{self.user_name} created on {self.user_created_date.ctime()}'

class Post(models.Model):
    # TODO: add post url later
    class Category(models.TextChoices):
        PLAIN_TEXT = "Plain Text"
        JAVASCRIPT = "JavaScript"
        PYTHON = "Python"
        OTHER_Language = "Other Language"

    class Type(models.TextChoices):
        NOTES = "Notes"
        CODE = "Code"
        TEMP = "Temporary File"

    post_title = models.CharField(max_length=50)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_content = models.TextField(max_length=4096)
    post_description = models.CharField(max_length=50)
    post_category = models.CharField(max_length=14, choices=Category.choices, default=Category.PLAIN_TEXT) 
    post_type = models.CharField(max_length=14, choices=Type.choices, default=Type.NOTES)
    post_created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.post_title} by {self.post_author.user_name} created on {self.post_created_date.ctime()}'