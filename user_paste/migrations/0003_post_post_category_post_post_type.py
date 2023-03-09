# Generated by Django 4.1.7 on 2023-03-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_paste', '0002_user_post_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_category',
            field=models.CharField(choices=[('Plain Text', 'Plain Text'), ('JavaScript', 'Javascript'), ('Python', 'Python')], default='Plain Text', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('Notes', 'Notes'), ('Code', 'Code'), ('Temp File', 'Temp')], default='Notes', max_length=10),
        ),
    ]
