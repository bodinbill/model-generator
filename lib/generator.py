from template.interface import InterfaceTemplate
from reader import Reader

class Generator:
    def __init__(self, filename):
        self.reader = Reader(filename)

    def execute(self):
        self.reader.execute()
        datas=self.reader.getData()

        tps=[InterfaceTemplate(datas)]

        for tp in tps:
            print tp.execute()
                
