# Generated by Django 4.1.1 on 2022-09-14 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chatroom_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name_plural': 'Messages'},
        ),
    ]
