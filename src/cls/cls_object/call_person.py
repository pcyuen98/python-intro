#create object
from cls.cls_object.person import Person

person = Person()
person.name = 'Andy'
person.address = 'My New Address'

print('name--->' , person.name  )
print('address--->', person.address )
print ('Full Name-->' , person.get_sentense())


