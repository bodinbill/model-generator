class Reader:
    def __init__(self, filename):
        self.filename=filename
        self.data=[]
        
    def execute(self):
        f=open(self.filename,"r")

        for line in f.readlines():
            if line.count("=") and len(line.strip()) > 3:
                d=self._split(line,"=")
                self._execute(d[0],d[1])

    def _split(self,value,separator):
        d=value.strip().split(separator)
        return (d[0].strip(),d[1].strip())

    def _execute(self,name,value):
        self.data.append((name,value))

    def getData(self):
        return self.data

        
    
