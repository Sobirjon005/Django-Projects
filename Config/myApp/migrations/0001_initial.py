# Generated by Django 5.0.2 on 2024-05-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaqolaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('tags', models.CharField(choices=[('World', 'World'), ('Local', 'Local'), ('Sport', 'Sport')], max_length=255)),
            ],
        ),
    ]
