from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _T
import abc

# Create your models here.

class Equipment(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    description=models.TextField()

class PluginApp(Equipment):
    owner=models.ForeignKey(Equipment, related_name="app")

    
class Logline(models.Model):
    timestamp=models.DateTimeField('Logs reporting time')
    pluin_app=models.ForeignKey(PluginApp, related_name='Logs')
    log_text=models.TextField()
    level=models.CharField(max_length=50,
                           help_text=_T("Importance of the logline") )

    @abc.abstractmethod
    def get_log_key(self):
        pass

    @abc.abstractmethod
    def get_log_value(self):
        pass
   
    @abc.abstractmethod
    def get_instance(self):
        pass
