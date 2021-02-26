from cls.cls_object.person import Person
from cls.server.json_server_method import JSONServerClass
class JSONServerSearch:
    
    @staticmethod
    def searchName(user_input):
        print('searching for-->' , user_input.name)
        for person in JSONServerClass.getPerson():
            personLocal = Person()
            personLocal.__dict__ = person
            print('personLocal name-->' , personLocal.name)
            isMatch = personLocal.name == user_input.name
            print('isMatch ? -->' , isMatch)
            if isMatch:
                return True
        return False
    
    @staticmethod
    def searchAddress(user_input):
        # complete the method below
        print('searching address for-->' , user_input.address)

        return False