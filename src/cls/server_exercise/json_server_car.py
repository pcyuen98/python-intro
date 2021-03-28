from cls.server_exercise.json_server_method_car import JSONServerCarClass
from cls.server_exercise.json_server_search_car import JSONServerCarSearch
import json


URLS = (
    '/car/get', 'JsonGet',
    '/car/post', 'JsonPost',
    '/car/search', 'JsonSearch'        
)

# URL Get - http://localhost:8080/car/get
# URL Post - http://localhost:8080/car/post
# URL Search - http://localhost:8080/car/search?model=kancil

# Sample Json - {'brand': 'Produa', 'modal': 'kancil'}

class JsonGet(object):

    def GET(self):
        carInJsonString = json.dumps(JSONServerCarClass.getCar())
        print('return json-->' , carInJsonString )
        return carInJsonString

class JsonPost(object):

    def POST(self):
        import web
        print('post started')
        json_data = web.data()
        
        return JSONServerCarClass.setCar(json_data)

class JsonSearch(object):
    
    def GET(self):
        import web
        # Exercise: Complete the method below 
        user_input = web.input()
        isCarModelExist = JSONServerCarSearch.searchModel(user_input.model)
        
        return isCarModelExist
        
def main():
    """
    Main function starting app
    """
    import web 
    http_app = web.application(URLS, globals())
    http_app.run()

if __name__ == "__main__":
    main()