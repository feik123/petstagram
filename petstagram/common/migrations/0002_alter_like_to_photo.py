# Generated by Django 4.2.16 on 2024-11-04 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_photo'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='to_photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.photo'),
        ),
    ]
