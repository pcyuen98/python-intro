# more example - https://www.w3schools.com/python/python_classes.asp
from cls.cls_object.person import Car

class JSONServerCarClass:
    
    cars = [];
    
    @staticmethod
    def getCar():
        
        print ('persons--->' , JSONServerCarClass.cars) 
        return JSONServerCarClass.cars        
            
    @staticmethod
    def setPerson(json_data):
        
        import json
        person = json.loads(json_data)
        print ('data received ====' , person)        
        
        # convert received person to local person Object
        personLocal = Car()
        personLocal.__dict__ = person
        print ('received person--->' , person)
                    
        print ('personLocal Name--->' , personLocal.brand)
        print ('personLocal address--->' , personLocal.model)
        
        JSONServerCarClass.cars.append(person)       
         
        print ('after add persons--->' , JSONServerCarClass.persons)
        return JSONServerCarClass.persons
