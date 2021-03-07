from cls.cls_object.person import Car
from cls.server.json_server_method import JSONServerClass
from cls.server_exercise.json_server_method_car import JSONServerCarClass
class JSONServerSearch:
    
    @staticmethod
    def searchName(user_input):
        print('searching for-->' , user_input.brand)
        for person in JSONServerCarClass.getCar():
            carLocal = Car()
            personLocal.__dict__ = person
            print('personLocal name-->' , personLocal.brand)
            isMatch = personLocal.brand == user_input.brand
            print('isMatch ? -->' , isMatch)
            if isMatch:
                return True
        return False
    
    @staticmethod
    def searchAddress(user_input):
        # complete the method below
        print('searching address for-->' , user_input.model)

        return False