# Generated by Django 5.0.2 on 2024-06-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forOrdering', '0007_alter_order_customer_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=33),
        ),
    ]
