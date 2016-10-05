from lib.generator import Generator

def main():
    templetes = ["Interface" , "Implement" , "Test" , "RepositoryHibernateTest", "Form", "FormTest" ,
                "Filter" , "FilterTest", "AdminController", "AdminControllerTest" , "CreateForm", "CreateFormTest",
                "UpdateForm", "UpdateFormTest", "WebModel", "WebModelTest"]
    
    Generator("config.txt", templetes).execute()

if  __name__ == '__main__':main()
