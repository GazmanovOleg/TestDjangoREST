# Generated by Django 4.2 on 2023-04-11 10:39

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_file_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='filename',
            field=models.CharField(default='string', max_length=255),
        ),
        migrations.AlterField(
            model_name='file',
            name='height',
            field=models.IntegerField(blank=True, validators=[core.models.width_or_height_vaildator]),
        ),
        migrations.AlterField(
            model_name='file',
            name='processing',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='width',
            field=models.IntegerField(blank=True, validators=[core.models.width_or_height_vaildator]),
        ),
    ]