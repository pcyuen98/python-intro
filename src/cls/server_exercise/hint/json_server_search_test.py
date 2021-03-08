from cls.server.json_server_method import JSONServerClass
from cls.cls_object.car import Car


class JSONServerSearchTest:

    @staticmethod
    # Input address to search here . i.e. "Selangor"
    def searchAddress(address):
        
        # Looping of the json list in the memory. 
        # In this example, it has only 1 loop cause got 1 data only
        for person in JSONServerClass.getPerson():
            
            # Convert into Json Object First from Json String
            personLocal = Car()
            personLocal.__dict__ = person
            
            # Compare the input "Selangor" with data inside memory 
            isMatch = personLocal.model == address
            
            if isMatch:
                return True
        return False
    
# Load the Memory for string value below
# This is to skip the Server Process 
JSONServerClass.setPerson('{"name":"Kiruban","address":"Selangor"}')

print('\n')
address = 'Selangor1'
print(address , ' value Matching? --->' , JSONServerSearchTest.searchAddress(address))

print('\n')
address = 'Selangor'
print(address , ' value Matching? --->' , JSONServerSearchTest.searchAddress(address))
