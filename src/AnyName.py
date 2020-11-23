import datetime

# dictionary Value
dictionaryValue = {'one': '11', 'two': '22', 'three': '33'}



for key in dictionaryValue :
    if dictionaryValue[key] == '11': print ('the value is 11'  )
    else: print ('not match')

before = datetime.datetime.now()

myset = ["1", "2", "3"]

for _ in range(10000000):
    myset.append(datetime.datetime.now())

print("myset length-->" , len(myset))     
   
after = datetime.datetime.now()

print ('time taken in seconds--->', (after - before).seconds)