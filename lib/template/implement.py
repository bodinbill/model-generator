from template import Template, TemplateUtils
import tptype

class ImplementTemplate(Template):
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
        
        return tptype.IMPLEMENT_TEMPLATE%\
              (datas["package"],upper,datas["author"],upper,datas["abstract"],datas["key"],upper,privates,methods)

    def _generateGetMethod(self,name,type):
        upper=TemplateUtils.splitUpper(name,"")
        
        return tptype.GET_METHOD_IMPL_TEMPLATE%(type,upper,name)

    def _generateIsMethod(self,name,type):
        upper=TemplateUtils.splitUpper(name,"")
        
        return tptype.IS_METHOD_IMPL_TEMPLATE%(type,upper,name)

    def _generateSetMethod(self,name,type):
        upper=TemplateUtils.splitUpper(name,"")
        
        return tptype.SET_METHOD_IMPL_TEMPLATE%(upper,type,name,name,name)

