# Generated by Django 3.2 on 2021-04-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameo', '0004_auto_20210411_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='cameo',
            name='is_featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='cameo',
            name='currency_code',
            field=models.CharField(choices=[('USD', '$'), ('INR', '₹'), ('GBP', '£'), ('EUR', '€')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cameo',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
