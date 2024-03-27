# Generated by Django 3.0.7 on 2024-03-27 11:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20240327_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='designation',
            field=models.CharField(default='user', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(default='http://facebook.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='first_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='google_plus_link',
            field=models.URLField(default='http://google.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='last_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='photo',
            field=models.ImageField(default='', upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(default='http://twitter.com', max_length=100),
            preserve_default=False,
        ),
    ]