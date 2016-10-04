from template import Template, TemplateUtils

class RepositoryHibernateTestTemplate(Template):
    def __init__(self, datas):
        super(self.__class__, self).__init__(datas);

    def execute(self):
        datas = self.getDatas()

        entityName = datas["name"]

        return TemplateUtils.get("test-repository-hibernate").format(entityName)
