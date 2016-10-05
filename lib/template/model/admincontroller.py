from lib.template.template import TemplateUtils, Template

class AdminControllerTemplate(Template):
    def __init__(self, datas):
        super(self.__class__, self).__init__(datas)

    def execute(self):
        datas = self.getDatas()
        name = datas["name"]
        
        columns = "\"entity.id\""
        
        for data in self.getProperties():
            columns += ", \"entity.%s\"" % data[0]
        
        camel = TemplateUtils.splitCamel(name)
        entityName = TemplateUtils.splitUpper(name, "-").lower()
        upper = TemplateUtils.splitUpper(name, "")
        lower = TemplateUtils.splitLower(name)
        
        return TemplateUtils.get("admin-controller").format(packet=datas["package"], key=datas["key"], columns=columns, \
                                                            camel=camel, interface=upper, entityName=entityName, name=lower)
