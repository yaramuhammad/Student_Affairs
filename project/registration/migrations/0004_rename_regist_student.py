# Generated by Django 4.0.4 on 2022-05-17 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_alter_regist_status_alter_regist_studentlevel_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Regist',
            new_name='Student',
        ),
    ]
