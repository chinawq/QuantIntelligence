from django.db import models

# Create your models here.

class HistData(models.Model):
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=30)
    data_owner = models.CharField(max_length=128)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    data_type = models.CharField(max_length=30)
    data_frequency = models.CharField(max_length=30)
    data_file_path = models.FileField(upload_to='./hist_data/')