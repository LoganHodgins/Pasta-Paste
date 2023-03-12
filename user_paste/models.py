from django.utils.crypto import get_random_string
from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=20, unique=True)
    user_created_date = models.DateTimeField(auto_now_add=True)
    # TODO: add password

    def __str__(self):
        return f'{self.user_name} created on {self.user_created_date.ctime()}'

class Post(models.Model):
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
    post_url_slug = models.SlugField(null=True, unique=True)
    
    def generate_random_unique_slug(self):
        while True:
            random_str = get_random_string(8, '0123456789')
            slug = self.post_author.user_name.strip() + '-' + random_str
            rows_with_slug = type(self).objects.filter(post_url_slug=slug)
            if len(rows_with_slug) == 0:
                return slug

    def save(self, *args, **kwargs):
        if not self.post_url_slug:
            self.post_url_slug = self.generate_random_unique_slug()
            super(Post, self).save(*args, **kwargs)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.post_title} by {self.post_author.user_name} created on {self.post_created_date.ctime()}'