# Generated by Django 5.0.4 on 2024-04-25 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0002_user_pessoa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_pessoa',
            old_name='FK_PESSOA_USER',
            new_name='FK_PESSOA',
        ),
        migrations.RenameField(
            model_name='user_pessoa',
            old_name='user_firebase_id',
            new_name='FK_USER',
        ),
    ]
