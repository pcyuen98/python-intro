import web
from client_server.web_sample import getWebMethod

urls = (
     '/', 'RootURL'    # the RootURL is mapping to the class name below on line 9

)

class RootURL:
    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        # return "hello Chrome 123!"        # return simple message
        return getWebMethod.sparePart()   # return GetMethod PY file and Spare Part method 

if __name__ == "__main__":                     # Standard Web Starter Instruction
    app = web.application(urls, globals())     # Mapping to line 4 'urls' variable to tell Python 
    app.run()                                  # Standard Web Starter Instruction

