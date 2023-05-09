# Generated by Django 4.2 on 2023-05-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_token',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='profile',
            name='dec',
            field=models.CharField(default='Bla Bla Bla.....', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='John Doe (Default)', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(default='Bla Bla Bla....', max_length=200, null=True),
        ),
    ]