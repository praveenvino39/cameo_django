# Generated by Django 3.2.9 on 2022-01-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameo', '0011_alter_cameo_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cameo',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]
