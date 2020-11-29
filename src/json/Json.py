import json

def loadJson():
    # some JSON:
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    # parse x:
    y = json.loads(x)
    # the result is a Python dictionary:
    print(y["age"])
    return y["age"]