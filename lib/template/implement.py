from template import Template, TemplateUtils

class ImplementTemplate(Template):
    def __init__(self, datas):
        super(self.__class__, self).__init__(datas)

    def execute(self):
        datas = self.getDatas()
        name = datas["name"]

        privates = ""
        for data in self.getProperties():
            privates += "	private %s %s;\n" % (data[1], data[0])

        prefix = ""
        methods = ""
        
        for data in self.getProperties():
            methods += prefix
            if data[1] == "boolean":
                methods += self._generateIsMethod(data[0], data[1])
            else:
                methods += self._generateGetMethod(data[0], data[1])

            prefix = "\n\n"
            methods += prefix
            methods += self._generateSetMethod(data[0], data[1])

        upper = TemplateUtils.splitUpper(name, "")
        
        return TemplateUtils.get("implement") % (datas["package"], upper, datas["author"], upper, \
                                                 datas["abstract"], datas["key"], upper, privates, methods)

    def _generateGetMethod(self, name, data_type):
        upper = TemplateUtils.splitUpper(name, "")
        
        return TemplateUtils.get("get-method-impl") % (data_type, upper, name)

    def _generateIsMethod(self, name, data_type):
        upper = TemplateUtils.splitUpper(name, "")
        
        return TemplateUtils.get("is-method-impl") % (data_type, upper, name)

    def _generateSetMethod(self, name, data_type):
        upper = TemplateUtils.splitUpper(name, "")
        
        return TemplateUtils.get("set-method-impl") % (upper, data_type, name, name, name)

