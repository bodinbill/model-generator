from template import Template 
from tptype import TemplateType

class RepositoryHibernateTestTemplate(Template):
    def __init__(self, datas):
        super(self.__class__, self).__init__(datas);

    def execute(self):
        datas = self.getDatas()

        entityName = datas["name"]

        return TemplateType.TEST_REPOSITORY_HIBERNATE_TEMPLATE.format(entityName)
