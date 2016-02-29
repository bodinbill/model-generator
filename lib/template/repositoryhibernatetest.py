from template import Template, TemplateUtils
import tptype

class RepositoryHibernateTestTemplate(Template):
    def __init__(self, datas):
        super(self.__class__, self).__init__(datas);

    def execute(self):
        datas = self.getDatas()

        entityName = datas["name"]

        return tptype.TEST_REPOSITORY_HIBERNATE_TEMPLATE.format(entityName)
