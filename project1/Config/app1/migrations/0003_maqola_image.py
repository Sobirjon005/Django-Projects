# Generated by Django 5.0.2 on 2024-04-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_maqola_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='maqola',
            name='image',
            field=models.ImageField(default=-1, upload_to=''),
            preserve_default=False,
        ),
    ]
