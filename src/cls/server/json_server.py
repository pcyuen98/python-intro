from cls.server.json_server_method import JSONServerClass
from cls.server.json_server_search import JSONServerSearch
URLS = (
    '/json/get', 'JsonGet',
    '/json/post', 'JsonPost',
    '/json/search', 'JsonSearch',
    '/json/search/address', 'JsonSearchAddress'
)


class JsonGet(object):

    def GET(self):
        return JSONServerClass.getPerson()

class JsonPost(object):

    def POST(self):
        
        import web

        print('post started')

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
        import web
        # Exercise: Complete the method below 
        user_input = web.input()
        # JSONServerSearch.searchAddress(None)
        isPersonAddressExist = JSONServerSearch.searchAddress(user_input)
        
        return isPersonAddressExist

def main():
    """
    Main function starting app
    """
    import web 

    http_app = web.application(URLS, globals())
    http_app.run()

if __name__ == "__main__":
    main()
