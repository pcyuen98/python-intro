from cls.cls_object.person import Person
from cls.server.json_server_method import JSONServerClass

class JSONServerSearch:
    
    @staticmethod
    def searchName(name):
        print('searching for-->' , name)
        for person in JSONServerClass.getPerson():
            personLocal = Person()
            personLocal.__dict__ = person
            print('personLocal name-->' , personLocal.name)
            isMatch = personLocal.name == name
            print('isMatch ? -->' , isMatch)
            if isMatch:
                return True
        return False
    
    @staticmethod
    def searchAddress(address):
        print('searching for-->' , address)
        # Complete this implementation here
        # the logic is similar to searchName method above. 
        # You may copy line 9 to 16 from above, paste here then modify it 
        return False

# Load the Memory for string value below
# This is to skip the Server Process 

JSONServerClass.setPerson('{"name":"Kiruban","address":"Selangor"}')

print('\n')
name = 'Kiruban'
print(name , ' name Matching? --->' , JSONServerSearch.searchName(name))

print('\n')
address = 'Selangor1'
print(address , ' address Matching? --->' , JSONServerSearch.searchAddress(address))