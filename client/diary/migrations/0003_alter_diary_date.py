# Generated by Django 4.0.5 on 2022-07-07 07:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_rename_like_diary_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
