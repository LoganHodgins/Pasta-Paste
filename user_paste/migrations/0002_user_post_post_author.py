# Generated by Django 4.1.7 on 2023-03-09 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_paste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_paste.user'),
        ),
    ]
