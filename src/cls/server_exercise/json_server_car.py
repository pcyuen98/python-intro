from cls.server.json_server_method import JSONServerClass
from cls.server.json_server_search import JSONServerSearch
URLS = (
    '/car/get', 'JsonGet',
    '/car/post', 'JsonPost',
    '/car/search', 'JsonSearch'
    '/car/search/address', 'JsonSearchAddress'
)


class JsonGet(object):

    def GET(self):
        return JSONServerClass.getPerson()

class JsonPost(object):

    def POST(self):
        import web
        json_data = web.data()
        
        return JSONServerClass.setPerson(json_data)

class JsonSearch(object):
    
    def GET(self):
        import web 
        user_input = web.input()

        isPersonNameExist = JSONServerSearch.searchName(user_input)
        
        return isPersonNameExist

class JsonSearchAddress(object):
    
    def GET(self):
        # Exercise: Complete the method below 
        JSONServerSearch.searchAddress(None)
        
        return False

class JsonSearchModel(object):
    
    def GET(self):
        import web
        # Exercise: Complete the method below 
        user_input = web.input()
        # JSONServerSearch.searchAddress(None)
        isCarModelExist = JSONServerSearch.searchModel(user_input)
        
        return isCarModelExist
    
class JsonSearchBrand(object):
    
    def GET(self):
        import web
        # Exercise: Complete the method below 
        user_input = web.input()
        # JSONServerSearch.searchAddress(None)
        isCarBrandExist = JSONServerSearch.searchBrand(user_input)
        
        return isCarBrandExist

       
        
def main():
    """
    Main function starting app
    """
    import web 
    http_app = web.application(URLS, globals())
    http_app.run()

if __name__ == "__main__":
    main()
