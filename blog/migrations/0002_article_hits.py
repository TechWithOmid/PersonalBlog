# Generated by Django 3.1.6 on 2021-02-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='blog.IPAddress', verbose_name='بازدیدها'),
        ),
    ]
