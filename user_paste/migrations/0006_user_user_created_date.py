# Generated by Django 4.1.7 on 2023-03-11 06:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_paste', '0005_alter_user_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]