from django.db import models

class BacktestingTask(models.Model):
    task_name = models.CharField(max_length=30)
    task_owner = models.CharField(max_length=128)
    task_strategy_list = models.CharField(max_length=10000)
    task_dataset_list = models.CharField(max_length=10000)
    task_policy = models.IntegerField()
    task_status = models.BooleanField()
    task_result = models.CharField(max_length=100000)
    task_create_time = models.DateTimeField(auto_now_add=True)
    task_modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['task_name','task_owner']]
