#create object
from cls.cls_object.person import Person
import json

person = Person()
person.name = 'My New Name'
person.address = 'My New Address'

#convert to JSON format in String
jsonStr = json.dumps(person.__dict__)

#print json string
print(jsonStr)

# convert to a JSON Object
jsonObj = json.loads(jsonStr)

print('name--->' + jsonObj["name"] )
print('address--->'  + jsonObj["address"] )

