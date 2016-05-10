

class logHandlerBase():
    def __init__(self):
        self._currentLogline=None
        self.logName=None
        self._logPtr=None

    def readLine(self):
        return None
        
    def readAll(self): 
        return None
            
    def parseLine(self, log):
        return None