# Generated by Django 4.2.4 on 2023-08-29 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_rename_queation_image_equation_equation_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Equation',
        ),
    ]