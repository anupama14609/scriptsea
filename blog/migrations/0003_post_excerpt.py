# Generated by Django 3.2.6 on 2021-09-06 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.CharField(default='', max_length=500),
        ),
    ]
