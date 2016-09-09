from template import Template, TemplateUtils
from tptype import TemplateType

class FilterTemplate(Template):
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
        requires = ""
        hashAppends = ""
        equalsAppends = ""
        
        for data in self.getProperties():
            upper = TemplateUtils.splitUpper(data[0], "")
            lower = TemplateUtils.splitCamel(data[0])
            if requires != "":
                requires += " || "
            requires += "has%s()" % upper
            
            hashAppends += ".append(%s)" % lower
            equalsAppends += "\t\t\tb.append(%s, rhs.%s);\n" % (lower, lower)
            
            methods += prefix
            methods += self._generateHasMethod(data[0], data[1])
            prefix = "\n\n"
            
            methods += prefix
            if data[1] == "boolean":
                methods += self._generateIsMethod(data[0], data[1])
            else:
                methods += self._generateGetMethod(data[0], data[1])

            methods += prefix
            methods += self._generateSetMethod(data[0], data[1])

        upper = TemplateUtils.splitUpper(name, "")
        lower = TemplateUtils.splitLower(name)
        camel = TemplateUtils.splitCamel(name)
        getterSetter = privates + "\n" + methods
        
        return TemplateType.FILTER_TEMPLATE.format(packet=datas["package"], interface=upper, auther=datas["author"], \
                                           entitykey=datas["key"], variable=getterSetter, name=lower, camel=camel, \
                                           required=requires, hashAppends=hashAppends, equalsAppends=equalsAppends)

    def _generateGetMethod(self, name, t):
        upper = TemplateUtils.splitUpper(name, "")
        lower = TemplateUtils.splitLower(name)
        
        return TemplateType.FORM_GET_METHOD_IMPL_TEMPLATE.format(ftype=t, upper=upper, name=name, callname=lower)

    def _generateIsMethod(self, name, t):
        upper = TemplateUtils.splitUpper(name, "")
        lower = TemplateUtils.splitLower(name)
        
        return TemplateType.FORM_IS_METHOD_IMPL_TEMPLATE.format(ftype=t, upper=upper, name=name, callname=lower)

    def _generateSetMethod(self, name, t):
        upper = TemplateUtils.splitUpper(name, "")
        lower = TemplateUtils.splitLower(name)
        
        return TemplateType.FORM_SET_METHOD_IMPL_TEMPLATE.format(ftype=t, upper=upper, name=name, callname=lower)

    def _generateHasMethod(self, name, t):
        upper = TemplateUtils.splitUpper(name, "")
        lower = TemplateUtils.splitLower(name)
        
        return TemplateType.FIlTER_HAS_METHOD_TEMPLATE.format(ftype=t, upper=upper, name=name, callname=lower)
