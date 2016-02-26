from ..reader import Reader
import re
import string
import tptype

class TemplateUtils:
    @staticmethod
    def split(identifier):
        regex='.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)'
        matches = re.finditer(regex, identifier)
        return [m.group(0) for m in matches]

    @staticmethod
    def splitLower(value):
        l=TemplateUtils.split(value)
        return string.join([f.lower() for f in l]," ")

    @staticmethod
    def splitUpper(value, separator=" "):
        l=TemplateUtils.split(value)
        return string.join([f.lower().upper()[0]+f.lower()[1:] for f in l],separator)

    @staticmethod
    def splitFull(value):
        l=TemplateUtils.split(value)
        return string.join([f.upper() for f in l],"_")
            
class Template(object):
    def __init__(self, datas):
        self.properties=[]
        self.datas={}
        for data in datas:
            if data[0].count("property"):
                name=data[0].split(":")[1]
                self.properties.append((name,data[1]))
            else:
                self.datas[data[0]]=data[1]

    def getDatas(self):
        return self.datas

    def getProperties(self):
        return self.properties
