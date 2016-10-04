from lib.template.template import TemplateUtils, Template
from lib.template.utils import Utils

class FormTestTemplate(Template):
    def __init__(self, datas):
        super(self.__class__, self).__init__(datas);

    def execute(self):
        datas = self.getDatas()
        name = datas["name"]
        
        labels = ""
        fill = ""
        fillForm = ""
        assertForm = ""
        create = ""
        assertNotForm = ""
        properties = Utils.formProperties(self.getProperties())  
        for data in properties:
            labels += self._generateLabels(data[0], data[1])
            
            fill += self._generateFill(name, data[0], data[1])
            fillForm += self._generateFillForm(data[0], data[1])
            assertForm += self._generateAssertForm(name, data[0], data[1])
            create += self._generateCreate(name, data[0], data[1])
            assertNotForm += self._generateAssertNotForm(name, data[0], data[1])
        
        upper = TemplateUtils.splitUpper(name, "")
        camel = TemplateUtils.splitCamel(name)
        
        return TemplateUtils.get("form-test").format(packet=datas["package"], entitykey=datas["key"], interface=upper, labelAmount=len(properties), \
                                                      camel=camel, labels=labels, fill=fill, fillForm=fillForm, assertForm=assertForm, \
                                                      create=create, assertNotForm=assertNotForm)

    def _generateAssertNotForm(self, cName, name, t):
        upper = TemplateUtils.splitUpper(name, "")
        variable = TemplateUtils.splitCamel(cName);
        return "            Assert.assertThat(underTest.get{upper}(), CoreMatchers.not(CoreMatchers.equalTo({name}.get{upper}())));\n"\
            .format(upper=upper, name=variable)
    
    def _generateCreate(self, cName, name, t):
        upper = TemplateUtils.splitUpper(name, "")
        variable = TemplateUtils.splitCamel(cName);
        return "            {name}.set{upper}({value});\n".format(upper=upper, name=variable, value=Utils.random(t))
    
    def _generateAssertForm(self, cName, name, t):
        upper = TemplateUtils.splitUpper(name, "")
        variable = TemplateUtils.splitCamel(cName);
        return "            Assert.assertThat(underTest.get{upper}(), CoreMatchers.equalTo({name}.get{upper}()));\n".format(upper=upper, name=variable)
    
    def _generateFillForm(self, name, t): 
        return "            underTest.set%s(%s);\n" % (TemplateUtils.splitUpper(name, ""), Utils.random(t))
    
    def _generateLabels(self, name, t): 
        label = TemplateUtils.splitUpper(name, " ")
        return "            Assert.assertThat(values.get(\"%s\"), CoreMatchers.equalTo(\"%s\"));\n" % (name, label)

    def _generateFill(self, cName, name, t):
        lower = TemplateUtils.splitCamel(cName)
        upper = TemplateUtils.splitUpper(name, "")
        return "            Assert.assertThat({name}.get{upper}(), CoreMatchers.equalTo(underTest.get{upper}()));\n".format(upper=upper, name=lower)
