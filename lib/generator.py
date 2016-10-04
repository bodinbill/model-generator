import os
import re

from reader import Reader
from template.filter import FilterTemplate
from template.filtertest import FilterTestTemplate
from template.form import FormTemplate
from template.implement import ImplementTemplate
from template.interface import InterfaceTemplate
from template.repositoryhibernatetest import RepositoryHibernateTestTemplate
from template.test import TestTemplate
from template.tptype import TemplateType


class Generator:
    def __init__(self, filename):
        self.reader = Reader(filename)
        self._collectTemplate()
   
    def _collectTemplate(self):
        TemplateType.GET_METHOD_TEMPLATE = self._collect("get-method") 
        TemplateType.SET_METHOD_TEMPLATE = self._collect("set-method")
        TemplateType.IS_METHOD_TEMPLATE = self._collect("is-method")
        TemplateType.INTERFACE_TEMPLATE = self._collect("interface")
        TemplateType.IMPLEMENT_TEMPLATE = self._collect("implement")
        TemplateType.GET_METHOD_IMPL_TEMPLATE = self._collect("get-method-impl")
        TemplateType.SET_METHOD_IMPL_TEMPLATE = self._collect("set-method-impl")
        TemplateType.IS_METHOD_IMPL_TEMPLATE = self._collect("is-method-impl")
        TemplateType.TEST_TEMPLATE = self._collect("test")
        TemplateType.TEST_METHOD_TEMPLATE = self._collect("test-method")
        TemplateType.TEST_IS_METHOD_TEMPLATE = self._collect("test-is-method")
        TemplateType.TEST_REPOSITORY_HIBERNATE_TEMPLATE = self._collect("test-repository-hibernate")
        TemplateType.FORM_TEMPLATE = self._collect("form")
        TemplateType.FORM_GET_METHOD_IMPL_TEMPLATE = self._collect("form-get-method-impl")
        TemplateType.FORM_SET_METHOD_IMPL_TEMPLATE = self._collect("form-set-method-impl")
        TemplateType.FORM_IS_METHOD_IMPL_TEMPLATE = self._collect("form-is-method-impl")
        TemplateType.FILTER_TEMPLATE = self._collect("filter")
        TemplateType.FIlTER_HAS_METHOD_TEMPLATE = self._collect("filter-has-method")
        TemplateType.FILTER_TEST_TEMPLATE = self._collect("filter-test")
        TemplateType.FILTER_METHOD_TEST = self._collect("filter-method-test")
        
    def _collect(self, filename):
        return open("./static/tpfile/%s.tp" % filename, "r").read()
    
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
        datas = self.reader.getData()

        tps = [InterfaceTemplate(datas), ImplementTemplate(datas), \
             TestTemplate(datas), RepositoryHibernateTestTemplate(datas), \
             FormTemplate(datas), FilterTemplate(datas), FilterTestTemplate(datas)]
        
        files = {}

        for tp in tps:
            body = tp.execute()
            
            m = re.search("public (class|interface) (\S+)", body)
            name = m.group(2)
            
            files[name] = body
            
        self._write(files)
        
            
            
            
            
