# Generated by Django 4.2.4 on 2023-08-29 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_projects_equation_paragraph_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equation',
            old_name='queation_image',
            new_name='equation_image',
        ),
    ]
