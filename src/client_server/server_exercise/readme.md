# Description
This is a exercise derive from the person json server as URL https://github.com/pcyuen98/python-intro/tree/main/src/cls/cls_object

# Exercise no.1 
Refer to the Web PY server class below, add additional API to search address instead of name <p>
https://github.com/pcyuen98/python-intro/blob/main/src/client_server/server/json_server.py

You will need to modify and complete the implementation below 

````

class JsonSearchAddress(object):
    
    def GET(self):
        # Exercise: Complete the method below 
        JSONServerSearch.searchAddress(None)
        
        return False
````

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
<p>
&emsp; https://github.com/pcyuen98/python-intro/blob/main/src/cls/cls_object/car.py

2. It should have 3 basic API function.

&emsp; &emsp; a. Post an object

&emsp; &emsp; b. Get all object in a list

&emsp; &emsp; c. search the brand name

Sample Json Object as below

````

{
   "brand":"Proton",
   "modal":" Perdana"
}

````