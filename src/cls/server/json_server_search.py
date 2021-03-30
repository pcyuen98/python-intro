from cls.cls_object.person import Person
from cls.server.json_server_method import JSONServerClass

class JSONServerSearch:
    
    @staticmethod
    def searchName(name):
        print('searching for-->' , name)
        for person in JSONServerClass.getPerson(): # For Loop, 1 record loop 1 time, 2 records loop 2 times
            personLocal = Person() # new object creation
            personLocal.__dict__ = person # convert to json
            print('personLocal name-->' , personLocal.name) # printing person name 
            isMatch = personLocal.name == name # is input == to the json object?  {'name': 'Kiruban', 'address': 'Selangor'}
            print('isMatch ? -->' , isMatch) 
            if isMatch:   # isMatch is true? 
                return True
        return False
    
    @staticmethod
    def searchAddress(address):
        print('searching for address-->' , address)
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
address = 'Selangor'
print(address , ' address Matching? --->' , JSONServerSearch.searchAddress(address))