# Generated by Django 3.1.6 on 2021-02-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210211_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]