# Generated by Django 3.1.7 on 2021-03-29 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_messenger', '0002_auto_20210329_0920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['updated_at']},
        ),
    ]
