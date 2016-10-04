import os
import re

from reader import Reader
from template.filter import FilterTemplate
from template.filtertest import FilterTestTemplate
from template.form import FormTemplate
from template.formtest import FormTestTemplate
from template.implement import ImplementTemplate
from template.interface import InterfaceTemplate
from template.repositoryhibernatetest import RepositoryHibernateTestTemplate
from template.test import TestTemplate

class Generator:
    def __init__(self, configFile):
        self.reader = Reader(configFile)
        
    def _templateList(self):
        datas = self.reader.getData()
        
        return [InterfaceTemplate(datas), ImplementTemplate(datas), TestTemplate(datas), \
                RepositoryHibernateTestTemplate(datas), FormTemplate(datas), FormTestTemplate(datas), \
                FilterTemplate(datas), FilterTestTemplate(datas)]
   
    
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
        
            
            
            
            
