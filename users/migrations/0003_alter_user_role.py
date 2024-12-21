# Generated by Django 5.0.10 on 2024-12-21 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('moderator', 'moderator'), ('member', 'member')], default='member', max_length=9, verbose_name='Role'),
        ),
    ]
