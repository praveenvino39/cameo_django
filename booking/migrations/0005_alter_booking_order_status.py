# Generated by Django 3.2.9 on 2021-12-22 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20210423_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='order_status',
            field=models.CharField(choices=[('initiated', 'Initiated'), ('pending', 'Pending'), ('completed', 'Completed'), ('Completed Request', 'Completed Request')], max_length=50),
        ),
    ]
