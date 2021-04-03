from cls.cls_object.person import Person
from cls.server.json_server_method import JSONServerClass
from pickle import TRUE

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
        print('Input address-->' , address)
        for person in JSONServerClass.getPerson():
            personLocal = Person() # new object creation
            personLocal.__dict__ = person # convert to json
            print ('\n') 
            print ('personLocal address -->', personLocal.address)
            #isBlackPrint = personLocal.name == 'BLACKPINK'
            #print ('isBlackPrint --->' , isBlackPrint)
            
            isMatching = personLocal.address == address
            print ('isMatching --->' , isMatching)
            
            if (isMatching):
                return True
        return False
    
    @staticmethod
    def searchPostCode(address):
        print('Input address-->' , address)
        for person in JSONServerClass.getPerson():
            personLocal = Person() # new object creation
            personLocal.__dict__ = person # convert to json
            print ('\n') 
            print ('personLocal address -->', personLocal.address)
            #isBlackPrint = personLocal.name == 'BLACKPINK'
            #print ('isBlackPrint --->' , isBlackPrint)
            
            isMatching = personLocal.address == address
            print ('isMatching --->' , isMatching)
            
            if (isMatching):
                return True
        return False
            
# Load the Memory for string value below
# This is to skip the Server Process 

JSONServerClass.setPerson('{"name":"Kiruban","address":"Selangor","postcode":"10000" }')

JSONServerClass.setPerson('{"name":"BLACKPINK","address":"mumbai","postcode":"250"}')
JSONServerClass.setPerson('{"name":"MAMAMOO","address":"SEOUL","postcode":"1999"}')

print('\n')
address = 'mumbai'
print(address , ' address exist? --->' , JSONServerSearch.searchAddress(address))