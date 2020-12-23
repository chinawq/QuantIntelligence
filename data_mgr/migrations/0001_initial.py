# Generated by Django 3.1.2 on 2020-12-22 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=30)),
                ('data_owner', models.CharField(max_length=128)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('data_type', models.CharField(max_length=30)),
                ('data_frequency', models.IntegerField()),
                ('data_file_path', models.FileField(upload_to='./hist_data/')),
            ],
        ),
    ]
