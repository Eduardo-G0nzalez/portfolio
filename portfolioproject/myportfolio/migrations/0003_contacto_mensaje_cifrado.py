# Generated by Django 4.2.13 on 2024-06-18 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='mensaje_cifrado',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
