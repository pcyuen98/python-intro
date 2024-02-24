from mysql.server.address import Address
import json
class Agent:
    
    name = 'A Name'
    address = 'An Address'
    postcode = 'An postcode'

    fullName = None
    email = None
    contactNumber = None 
    address = Address();

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        
    def get_sentense(self):
        print('self.name-->', self.name)
        if self.name == 'Andy':
            return 'He is Andy';     