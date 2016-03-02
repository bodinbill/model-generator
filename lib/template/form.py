from template import Template, TemplateUtils
import tptype

class FormTemplate(Template):
    def __init__(self, datas):
        super(self.__class__, self).__init__(datas)

    def execute(self):
        datas=self.getDatas()
        name=datas["name"]

        privates=""
        for data in self.getProperties():
            privates+="	private %s %s;\n"%(data[1],data[0])

        prefix=""
        methods=""
        
        for data in self.getProperties():
            methods+=prefix
            if data[1] == "boolean":
                methods+=self._generateIsMethod(data[0],data[1])
            else:
                methods+=self._generateGetMethod(data[0],data[1])

            prefix="\n\n"
            methods+=prefix
            methods+=self._generateSetMethod(data[0],data[1])

        upper=TemplateUtils.splitUpper(name,"")
        lower=TemplateUtils.splitLower(name)
        camel=TemplateUtils.splitCamel(name)
        getterSetter=privates+"\n"+methods
        
        return tptype.FORM_TEMPLATE.format(packet=datas["package"], interface=upper, auther=datas["author"],\
                                           entitykey=datas["key"],variable=getterSetter,name=lower,camel=camel,\
                                           fill="")

    def _generateGetMethod(self,name,t):
        upper=TemplateUtils.splitUpper(name,"")
        lower=TemplateUtils.splitLower(name)
        
        return tptype.FORM_GET_METHOD_IMPL_TEMPLATE.format(ftype=t,upper=upper,name=name,callname=lower)

    def _generateIsMethod(self,name,t):
        upper=TemplateUtils.splitUpper(name,"")
        lower=TemplateUtils.splitLower(name)
        
        return tptype.FORM_IS_METHOD_IMPL_TEMPLATE.format(ftype=t,upper=upper,name=name,callname=lower)

    def _generateSetMethod(self,name,t):
        upper=TemplateUtils.splitUpper(name,"")
        lower=TemplateUtils.splitLower(name)
        
        return tptype.FORM_SET_METHOD_IMPL_TEMPLATE.format(ftype=t,upper=upper,name=name,callname=lower)

