# Generated by Django 5.0.2 on 2024-06-14 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forProduct', '0009_rename_name_category_nameofcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='nameOfCategory',
            new_name='name',
        ),
    ]
