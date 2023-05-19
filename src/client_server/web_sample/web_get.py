import web
from client_server.web_sample import getWebMethod

urls = (
     '/', 'index1'    # the index1 is mapping to the class name below on line 4

)

class index1:
    def GET(self):

        # return "hello Chrome 123!"        # return simple message
        user_input = web.input()
        
        if user_input.__len__() > 0:
            selection = user_input.selection;
            print ('selection is-->' , selection)
        
        return getWebMethod.sparePart()   # return GetMethod PY file and Spare Part method 

if __name__ == "__main__":                     # Standard Web Starter Instruction
    app = web.application(urls, globals())     # Mapping to line 4 'urls' variable to tell Python 
    app.run()                                  # Standard Web Starter Instruction

