import requests

def printGet(): 
    response = requests.get('http://localhost:8080/')
    print(response.text)
    
printGet()    