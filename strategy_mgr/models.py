from django.db import models

# Create your models here.
class Strategy(models.Model):
    stg_name =  models.CharField(max_length=30) 
    stg_owner = models.CharField(max_length=128)
    stg_description = models.CharField(max_length=512)
    stg_create_time = models.DateTimeField(auto_now_add=True)
    stg_modify_time = models.DateTimeField(auto_now=True)
    stg_file_path = models.FileField(upload_to='./strategy/')

    class Meta:
        unique_together = [['stg_name','stg_owner']]

class StrategyServer(models.Model):
    stg_server_name = models.CharField(max_length=30,unique=True)
    stg_server_owner = models.CharField(max_length=128)
    stg_server_ip_addr = models.CharField(max_length=30,unique=True)
    stg_server_ip_port = models.CharField(max_length=5)
