import random
import string
from lib.template.template import TemplateUtils

class Utils:
    @staticmethod
    def formProperties(properties):
        data = []
        for name, t in properties:
            if t == "Name":
                data.append(("%sPrimary" % name, "String"))
                data.append(("%sThai" % name, "String"))
                data.append(("%sEnglish" % name, "String"))
            elif t == "Aliases":
                data.append((name, "String[]"))
            elif t == "int":
                data.append((name, "Integer"))
            elif t in ["boolean" , "long", "double"]:
                data.append((name, TemplateUtils.splitUpper(t, "")))
            else:
                data.append((name, t))
        return data
    
    @staticmethod
    def random(param_type):
        if param_type.count("[]"):
            none_array_type = param_type.replace("[]", "")
            
            values = ", ".join([Utils.random(none_array_type), Utils.random(none_array_type)])
            
            return "new %s[] {%s}" % (none_array_type, values)
        else:
            if param_type == "String":
                return "\"%s\"" % Utils._id_generator__private()
            if param_type == "int" or param_type == "Integer":
                return "%d" % int(Utils._id_generator__private(random.randint(2, 4), string.digits))
            if param_type.lower() == "long":
                return "%dL" % int(Utils._id_generator__private(random.randint(2, 4), string.digits))
            if param_type.lower() == "double":
                return "%d.%s" % (int(Utils._id_generator__private(random.randint(2, 4), string.digits)), \
                                  Utils._id_generator__private(2, string.digits))
        return "RANDOM_OBJECT"
        
    @staticmethod 
    def _id_generator__private(size=8, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
