import json

def loadJson():
    x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
    y = json.loads(x)
# the result is a Python dictionary:
    print(y["name"] + '---' + y["city"] + '---' + str(y["age"]) )
    return y["name"] + '---' + y["city"] + '---' + str(y["age"])

print(loadJson())