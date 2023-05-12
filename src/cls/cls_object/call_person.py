#create object
from cls.cls_object.person import Person
import json

person = Person()
person.name = 'My New Name'
person.address = 'My New Address'

#Print without Json 
print('-----Without Json section-----\n')

print('Without Json  name--->' , person.name  )
print('Without Json address--->', person.address )
print ('Full Name-->' , person.get_sentense())

#Print Using Json 
print('\n-----Json section-----\n')
#convert to JSON format in String
jsonStr = json.dumps(person.__dict__)

#print json string
print(jsonStr)

# convert to a JSON Object
jsonObj = json.loads(jsonStr)

print('Json  name--->' + jsonObj["name"] )
print(' Json address--->'  + jsonObj["address"] )


