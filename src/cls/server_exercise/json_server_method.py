# more example - https://www.w3schools.com/python/python_classes.asp
from cls.cls_object.person import Person

class JSONServerClass:
    
    persons = [];
    
    @staticmethod
    def getPerson():
        
        print ('persons--->' , JSONServerClass.persons) 
        return JSONServerClass.persons        
            
    @staticmethod
    def setPerson(json_data):
        
        import json
        person = json.loads(json_data)
        print ('data received ====' , person)        
        
        # convert received person to local person Object
        personLocal = Person()
        personLocal.__dict__ = person
        print ('received person--->' , person)
                    
        print ('personLocal Name--->' , personLocal.name)
        print ('personLocal address--->' , personLocal.address)
        
        JSONServerClass.persons.append(person)       
         
        print ('after add persons--->' , JSONServerClass.persons)
        return JSONServerClass.persons
