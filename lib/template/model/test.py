from lib.template.template import TemplateUtils, Template

class TestTemplate(Template):
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

        upper = TemplateUtils.splitUpper(name, "")
        
        return TemplateUtils.get("test") % \
              (datas["package"], upper, upper, methods)

    def _generateGetMethod(self, name, t):
        upper = TemplateUtils.splitUpper(name, "")
        full = TemplateUtils.splitFull(name)
        
        return TemplateUtils.get("test-method") % (upper, upper, upper, full, upper, full)

    def _generateIsMethod(self, name, t):
        upper = TemplateUtils.splitUpper(name, "")
        
        return TemplateUtils.get("test-is-method") % (upper, upper, upper, upper)


