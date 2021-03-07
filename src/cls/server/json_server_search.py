from cls.cls_object.person import Person
from cls.server.json_server_method import JSONServerClass
class JSONServerSearch:
    
    @staticmethod
    def searchName(user_input):
        print('searchName for-->' , user_input.name)
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
        print('searchAddress for-->' , user_input.address)
        for person in JSONServerClass.getPerson():
            print('searching person-->' , person)
            personLocal = person()
            personLocal.__dict__ = person
            print('personLocal address-->' , personLocal.address)
            isMatch = personLocal.address == user_input.address
            print('isMatch ? -->' , isMatch)
            if isMatch:
                return True
        return False