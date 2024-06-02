# Generated by Django 5.0.2 on 2024-05-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('surname', models.CharField(max_length=45)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=45)),
            ],
        ),
    ]
