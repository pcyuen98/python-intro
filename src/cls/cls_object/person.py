class Person:
    
    name = 'A Name'
    address = 'An Address'
    postcode = 'An postcode'

    def get_sentense(self):
        print('self.name-->', self.name)
        if self.name == 'My New Name':
            return 'He is Andy';     