# Generated by Django 4.0.5 on 2025-03-13 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_todoitem_image_todoitem_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='image_binary',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
