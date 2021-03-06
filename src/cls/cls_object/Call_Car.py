from cls.cls_object.car import Car
import json

car = Car()
car.brand = 'Car Brand'
car.model = 'Car Model'

#convert to JSON format in String
jsonStr = json.dumps(car.__dict__)

#print json string
print(jsonStr)

# convert to a JSON Object
jsonObj = json.loads(jsonStr)

print('brand--->' + jsonObj["brand"] )
print('model--->'  + jsonObj["model"] )