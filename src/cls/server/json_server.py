from cls.server.json_server_method import JSONServerClass
from cls.server.json_server_search import JSONServerSearch
import json
URLS = (
    '/json/get', 'JsonGet',
    '/json/post', 'JsonPost',
    '/json/search', 'JsonSearch',
    '/json/search/address', 'JsonSearchAddress'
)


class JsonGet(object):

    def GET(self):
        # need to convert to List Object to Json String else Angular cannot process it 
        personInJsonString = json.dumps(JSONServerClass.getPerson())
        print('return json-->' , personInJsonString )
        return personInJsonString

class JsonPost(object):

    def POST(self):
        
        import web

        print('post started')

        json_data = web.data()
        
        JSONServerClass.setPerson(json_data)
        
        # need to convert to List Object to Json String else Angular cannot process it 
        personInJsonString = json.dumps(JSONServerClass.getPerson())
        print('return json-->' , personInJsonString )
        
        return personInJsonString
        
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
