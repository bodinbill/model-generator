from template import Template, TemplateUtils

class InterfaceTemplate(Template):
    def __init__(self, datas):
        super(self.__class__, self).__init__(datas)

    def execute(self):
        datas = self.getDatas()
        name = datas["name"]

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

        upperName = TemplateUtils.splitUpper(name)
        upper = TemplateUtils.splitUpper(name, "")
        
        return TemplateUtils.get("interface") % \
              (datas["package"], upperName, datas["author"], upper, datas["super"], datas["key"], methods)

    def _generateGetMethod(self, name, data_type):
        lower = TemplateUtils.splitLower(name)
        upper = TemplateUtils.splitUpper(name, "")
        
        return TemplateUtils.get("get-method") % (lower, lower, data_type, upper)

    def _generateIsMethod(self, name, data_type):
        lower = TemplateUtils.splitLower(name)
        upper = TemplateUtils.splitUpper(name, "")
        
        return TemplateUtils.get("is-method") % (lower, lower, data_type, upper)

    def _generateSetMethod(self, name, data_type):
        lower = TemplateUtils.splitLower(name)
        upper = TemplateUtils.splitUpper(name, "")
        
        return TemplateUtils.get("set-method") % (lower, name, lower, upper, data_type, name)

