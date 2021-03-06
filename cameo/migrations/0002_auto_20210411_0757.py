# Generated by Django 3.0.6 on 2021-04-11 07:57

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cameo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cameo',
            name='bio',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='cameo',
            name='intro',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='cameo',
            name='fans',
            field=jsonfield.fields.JSONField(default='[]'),
        ),
        migrations.AlterField(
            model_name='cameo',
            name='reviews',
            field=jsonfield.fields.JSONField(default='[]'),
        ),
    ]
