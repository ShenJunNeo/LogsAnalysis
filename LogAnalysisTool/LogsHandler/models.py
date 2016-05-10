from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _T
import abc

# Create your models here.

    
class LogEvents(models.Model):
    flag=models.IntegerField()
    name=models.CharField(max_length=100)
    duration=models.DurationField()
    tempalte=models.TextField(default=None)

class TestRun(LogEvents):
    notes=models.TextField(default=None)
    testrun_result=models.CharField(max_length=15,default="Failed")
    testrun_case_link=models.URLField(max_length=100,default=None)
    
class Logline(models.Model):
    testrun=models.ForeignKey(TestRun, related_name="Logs",default=None) 
    log_text=models.TextField(default=None)

        
