# Generated by Django 3.1.6 on 2021-02-19 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='replycomment',
            old_name='body',
            new_name='reply_body',
        ),
    ]
