from template import Template, TemplateUtils
import tptype

class FilterTestTemplate(Template):
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
        properties=""
        
        for data in self.getProperties():
            upper=TemplateUtils.splitUpper(data[0],"")
            lower=TemplateUtils.splitCamel(data[0])
            properties+="filter.set%s(ANY_STRING);\n"%upper
            
            methods+=prefix
            methods+=tptype.FILTER_METHOD_TEST.format(upper=upper)
            prefix="\n\n"

        upper=TemplateUtils.splitUpper(name,"")
        getterSetter=privates+"\n"+methods
        
        return tptype.FILTER_TEST_TEMPLATE.format(packet=datas["package"], interface=upper, \
                                           testunit=methods,properties=properties)

