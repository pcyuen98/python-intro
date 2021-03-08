# more example - https://www.w3schools.com/python/python_classes.asp
from cls.cls_object.car import Car

class JSONServerCarClass:
    
    cars = [];
    
    @staticmethod
    def getCar():
        
        print ('car--->' , JSONServerCarClass.cars) 
        return JSONServerCarClass.cars        
            
    @staticmethod
    def setCar(json_data):
        
        import json
        car = json.loads(json_data)
        print ('data received ====' , car)        
        
        # convert received person to local person Object
        carLocal = Car()
        carLocal.__dict__ = car
        #print ('received car--->' , car)
                    
        #print ('carLocal Model--->' , carLocal.brand)
        #print ('carLocal Brand--->' , carLocal.model)
        
        JSONServerCarClass.cars.append(car)       
         
        #print ('after add cars--->' , JSONServerCarClass.car)
        return JSONServerCarClass.cars
