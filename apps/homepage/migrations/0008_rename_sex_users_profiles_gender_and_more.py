# Generated by Django 5.0.2 on 2024-03-05 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_users_profiles_benjamin_mark_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users_profiles',
            old_name='sex',
            new_name='gender',
        ),
        migrations.AddField(
            model_name='users_profiles',
            name='schoolType',
            field=models.CharField(default='NULL', max_length=10),
            preserve_default=False,
        ),
    ]
