# Generated by Django 4.2.16 on 2024-11-04 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_pet_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='pet_photo',
            new_name='personal_photo',
        ),
    ]
