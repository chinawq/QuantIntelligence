# Generated by Django 3.1.2 on 2020-12-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_mgr', '0002_auto_20201222_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='histdata',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='histdata',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]