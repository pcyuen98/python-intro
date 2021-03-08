from cls.cls_object.car import Car
from cls.server_exercise.json_server_method_car import JSONServerCarClass


class JSONServerCarSearch:
    

    
    @staticmethod
    def searchBrand(brand):  
        print('searching for-->' , brand)  
        for car in JSONServerCarClass.getCar():
            carLocal = Car()
            carLocal.__dict__ = car
            print('carLocal brand-->' , carLocal.brand)
            isMatch = carLocal.brand == brand
            print('isMatch ? -->' , isMatch)
            if isMatch:
                return True
        return False
    
    @staticmethod
    def searchModel(model):  
        print('searching for-->' , model)
        for car in JSONServerCarClass.getCar():
            carLocal = Car()
            carLocal.__dict__ = car
            print('carLocal model-->' , carLocal.model)
            isMatch = carLocal.model == model
            print('isMatch ? -->' , isMatch)
            if isMatch:
                return True
        return False