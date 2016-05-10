from .models import LogEvents, TestRun, Logline
from .logHandlerBase import logHandlerBase

class BetalGo(dict):
    def __init__(self):
        self.adapter=None
        self.testrun=None
        
    def setTestRun(self, testrun):
        if self._testrunValidator(testrun) is True:
            self.testrun=testrun

    def setLogsAdapter(self, adapter):
        if self._adapterValidator(adapter) is True:
            self.adapter=adapter
        raise RuntimeError("adapters must be sub class of class logHandlerBase")

    def _adapterValidator(self, adapter):        
        return issubclass(adapter,logHandlerBase)
    
    def _testrunValidator(self, testrun):
        return issubclass(testrun,TestRun)    
        

class logTemplateLoader(dict):
    pass
    
    
class LogEventsHunter(dict):
    def __init__(self, template, adapter):
        return None
    
    def _findFirstLog(self):
        return None
        
    def _findNextLog(self):
        return None
        
    def _findSliblingLogs(self):
        return None
        
    def findEventsFromLogs(self):
        return None
        