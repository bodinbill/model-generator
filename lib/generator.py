import os
import re

from reader import Reader

class Generator:
    def __init__(self, configFile, templetes):
        self.reader = Reader(configFile)
        self.templetes = templetes
        
    def _templateList(self):
        datas = self.reader.getData()
        
        return map(lambda tp : self._template_import__private(tp)(datas), self.templetes)
   
    def _template_import__private(self, model, filename=None):
        if not filename:
            filename = model.lower()
        name = "%sTemplate" % (model)
        
        mod = __import__("lib.template.model.%s" % filename, fromlist=[name])
        return  getattr(mod, name)
    
    def _write(self, files):
        path = "dist"
         
        if not os.path.exists(path):
            os.makedirs(path)
            
            
        for name, body in files.iteritems():
            f = open("%s/%s.java" % (path, name), "w")
            f.write(body)
            f.close()

        print "Generated file to %s" % os.path.abspath(path)

    def execute(self):
        self.reader.execute()

        tps = self._templateList()
        
        files = {}

        for tp in tps:
            body = tp.execute()
            
            m = re.search("public (class|interface) (\S+)", body)
            name = m.group(2)
            
            files[name] = body
            
        self._write(files)
        
            
            
            
            
