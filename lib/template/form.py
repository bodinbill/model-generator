from template import Template, TemplateUtils
from utils import Utils

TEMPLATE_PARAMETER_SET = """            if (isParameterSet("{param}", {param})) {{
                {name}.setCode({param});
            }}
"""
        
TEMPLATE_EXTRACT = """            if ({param} == null) {{
                {param} = {name}.get{upperParam}();
            }}
"""

class FormTemplate(Template):
    def __init__(self, datas):
        super(self.__class__, self).__init__(datas)

    def execute(self):
        datas = self.getDatas()
        name = datas["name"]

        privates = ""
        prefix = ""
        methods = ""
        fill = ""
        extract = ""
        labels = ""
        
        for data in Utils.formProperties(self.getProperties()):
            privates += "        private %s %s;\n" % (data[1], data[0])
            methods += prefix
            if data[1] == "boolean":
                methods += self._generateIsMethod(data[0], data[1])
            else:
                methods += self._generateGetMethod(data[0], data[1])

            prefix = "\n\n"
            methods += prefix
            methods += self._generateSetMethod(data[0], data[1])
            fill += self._generateFill(name, data[0], data[1])
            extract += self._generateExtract(name, data[0], data[1])
            labels += self._generateLabels(data[0], data[1])

        upper = TemplateUtils.splitUpper(name, "")
        lower = TemplateUtils.splitLower(name)
        camel = TemplateUtils.splitCamel(name)
        getterSetter = privates + "\n" + methods
        
        return TemplateUtils.get("form").format(packet=datas["package"], interface=upper, auther=datas["author"], \
                                           entitykey=datas["key"], variable=getterSetter, name=lower, camel=camel, \
                                           fill=fill, extract=extract, labels=labels)
    
    def _generateLabels(self, name, t): 
        label = TemplateUtils.splitUpper(name, " ")
        
        return "            labels.put(\"%s\", \"%s\");\n" % (name, label)
    
    def _generateFill(self, cName, name, t):
        lower = TemplateUtils.splitCamel(cName)
        return TEMPLATE_PARAMETER_SET.format(param=name, name=lower)
    
    def _generateExtract(self, cName, name, t):
        lower = TemplateUtils.splitCamel(cName)
        upper = TemplateUtils.splitUpper(name, "")
        return TEMPLATE_EXTRACT.format(param=name, name=lower, upperParam=upper)
     
    def _generateGetMethod(self, name, t):
        upper = TemplateUtils.splitUpper(name, "")
        lower = TemplateUtils.splitLower(name)
        
        return TemplateUtils.get("form-get-method-impl").format(ftype=t, upper=upper, name=name, callname=lower)

    def _generateIsMethod(self, name, t):
        upper = TemplateUtils.splitUpper(name, "")
        lower = TemplateUtils.splitLower(name)
        
        return TemplateUtils.get("form-is-method-impl").format(ftype=t, upper=upper, name=name, callname=lower)

    def _generateSetMethod(self, name, t):
        upper = TemplateUtils.splitUpper(name, "")
        lower = TemplateUtils.splitLower(name)
        
        return TemplateUtils.get("form-set-method-impl").format(ftype=t, upper=upper, name=name, callname=lower)

