# Generated by Django 5.0.2 on 2024-06-01 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_maqolamodel_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maqolamodel',
            name='link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
