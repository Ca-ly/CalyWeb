# Generated by Django 4.0.1 on 2022-02-24 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetsyauth', '0003_customusermodel_family_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customusermodel',
            old_name='given_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customusermodel',
            old_name='family_name',
            new_name='last_name',
        ),
    ]