# Generated by Django 3.1.2 on 2020-12-21 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy_mgr', '0002_auto_20201217_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrategyServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stg_server_name', models.CharField(max_length=30)),
                ('stg_server_ip_addr', models.CharField(max_length=30, unique=True)),
                ('stg_server_ip_port', models.CharField(max_length=5)),
            ],
        ),
    ]
