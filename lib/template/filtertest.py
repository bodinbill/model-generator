from template import Template, TemplateUtils

REQUIRE_TEMPLATE = """
		underTest.set{0}(null);
		Assert.assertThat(underTest.isRequired(), CoreMatchers.equalTo({1}));"""

class FilterTestTemplate(Template):
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
        properties = ""
        requires = ""
        p_list = self.getProperties()
        length = len(p_list)
        
        for i in range(length):
            last = i == length - 1
            data = p_list[i]
            
            upper = TemplateUtils.splitUpper(data[0], "")
            properties += "filter.set%s(TestCase.ANY_%s);\n" % (upper, data[1].upper())
            
            methods += prefix
            methods += TemplateUtils.get("filter-method-test").format(upper=upper, uppertype=data[1].upper())
            prefix = "\n\n"
            
            requires += REQUIRE_TEMPLATE.format(upper, str(not last).lower())

        upper = TemplateUtils.splitUpper(name, "")
        
        return TemplateUtils.get("filter-test").format(packet=datas["package"], interface=upper, \
                                           testunit=methods, properties=properties, requires=requires)

