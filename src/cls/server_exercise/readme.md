# Description
This is a exercise derive from the person json server as URL below
https://github.com/pcyuen98/python-intro/tree/main/src/cls/server

# Exercise no.1 
Refer to the Web PY server class below, add additional API to search address instead of name
https://github.com/pcyuen98/python-intro/blob/main/src/cls/server/json_server.py

You will need to modify and complete the implementation below 

class JsonSearchAddress(object):
    
    def GET(self):
        # Exercise: Complete the method below 
        JSONServerSearch.searchAddress(None)
        
        return False

It should able to search partial key words, i.e if "Penang" existed in the json list, then it should return true

http://localhost:8080/search/address?address=Penang

Sample Json
{
   "name":"Kap",
   "address":" Penang"
}

It must utilize the method below from the JSONServerClass
def searchAddress(user_input):

# Exercise no.2 
1. Instead of passing and getting the Person object. It should utilize Car object instead as per class below
https://github.com/pcyuen98/python-intro/blob/main/src/cls/cls_object/car.py

2. It should have 3 basic API function.
a. Post an object

b. Get all object in a list

c. search the brand name

Sample Json Object as below

{
   "brand":"Proton",
   "modal":" Perdana"
}