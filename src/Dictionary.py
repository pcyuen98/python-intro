
# dictionary
dictionary = {1: 'one', 2: 'two', 3: 'Three'}

print ('dictionary -->', dictionary)

print ('dictionary value at 1 -->', dictionary.get(3))


# dictionary Value
dictionaryValue = {'one': '11', 'two': '22', 'three': '33'}

print ('dictionary value -->', dictionaryValue.get('one'))

# dictionary LOOP
for key in dictionaryValue :
    print('loop  key--->', key, '  value--->',  dictionaryValue[key])

for key in dictionaryValue :
    if key == 'one': print ('the key is one'  )
    
for key in dictionaryValue :
    if dictionaryValue[key] == '11': print ('the value is 11'  )    