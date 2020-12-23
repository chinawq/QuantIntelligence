# Generated by Django 3.1.2 on 2020-12-17 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy_mgr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategy',
            name='stg_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='strategy',
            unique_together={('stg_name', 'stg_owner')},
        ),
    ]
