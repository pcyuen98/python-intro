from cls.server.json_server_method import JSONServerClass
from cls.server.json_server_search import JSONServerSearch
URLS = (
    '/get', 'JsonGet',
    '/post', 'JsonPost',
    '/search', 'JsonSearch',
    '/search/address', 'JsonSearchAddress'
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
        
        # JSONServerSearch.searchAddress(None)
        
        return False

def main():
    """
    Main function starting app
    """
    import web 
    http_app = web.application(URLS, globals())
    http_app.run()

if __name__ == "__main__":
    main()
