# update on 27 Jan 2021 - 9.33 pm

import datetime;

mylist = []

before = datetime.datetime.now()

for _ in range(10000000):
    mylist.append("datetime.datetime.now()")

print("List length-->" , len(mylist))     
   
after = datetime.datetime.now()

print ('Python time taken in seconds--->', (after - before).seconds)
