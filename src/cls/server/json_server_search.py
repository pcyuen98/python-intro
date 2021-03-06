from cls.cls_object.person import Car
from cls.server.json_server_method import JSONServerClass
class JSONServerSearch:
    
    @staticmethod
    def searchName(user_input):
        print('searching for-->' , user_input.brand)
        for person in JSONServerClass.getPerson():
            personLocal = Car()
            personLocal.__dict__ = person
            print('personLocal name-->' , personLocal.brand)
            isMatch = personLocal.brand == user_input.brand
            print('isMatch ? -->' , isMatch)
            if isMatch:
                return True
        return False
    
    @staticmethod
    def searchAddress(user_input):
        print('searching for-->' , user_input.model)
        #for person in JSONServerClass.getPerson():
        #    personLocal = Car()
        #    personLocal.__dict__ = person
        #    print('personLocal address-->' , personLocal.address)
        #    isMatch = personLocal.address == user_input.address
        #    print('isMatch ? -->' , isMatch)
        #    if isMatch:
        #        return True
        return False