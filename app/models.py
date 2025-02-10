from django.db import models

# Create your models here.


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.task_name 
    