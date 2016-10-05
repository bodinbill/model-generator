from lib.template.template import TemplateUtils, Template

class WebModelTemplate(Template):
    def __init__(self, datas):
        super(self.__class__, self).__init__(datas)

    def execute(self):
        datas = self.getDatas()
        name = datas["name"]
        
        camel = TemplateUtils.splitCamel(name)
        entityName = TemplateUtils.splitUpper(name, "-").lower()
        upper = TemplateUtils.splitUpper(name, "")
        lower = TemplateUtils.splitLower(name)
        
        return TemplateUtils.get("web-model").format(packet=datas["package"], key=datas["key"], \
                                                            camel=camel, interface=upper, entityName=entityName, name=lower)
