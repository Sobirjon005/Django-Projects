# Generated by Django 5.1.1 on 2024-10-07 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_remove_movie_actor_movie_actor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.actor'),
        ),
    ]
