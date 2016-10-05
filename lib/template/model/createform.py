from lib.template.template import TemplateUtils, Template

class CreateFormTemplate(Template):
    def __init__(self, datas):
        super(self.__class__, self).__init__(datas)

    def execute(self):
        datas = self.getDatas()
        upper = TemplateUtils.splitUpper(datas["name"], "")
        
        return TemplateUtils.get("create-form").format(packet=datas["package"], interface=upper)
