# Generated by Django 3.2.12 on 2023-11-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_merge_20231127_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='skills',
            field=models.ManyToManyField(to='main_app.Skill'),
        ),
    ]