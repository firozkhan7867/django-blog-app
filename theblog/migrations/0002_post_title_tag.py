# Generated by Django 3.2.2 on 2021-05-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='', max_length=255),
        ),
    ]
