import web

urls = (
     '/', 'index1'    # the index1 is mapping to the class name below on line 4

)

class index1:
    def GET(self):
        from web import getWebMethod                  # import something from GetMethod py File
        #return "hello Chrome 123!"        # return simple message
        return getWebMethod.sparePart()   # return GetMethod PY file and Spare Part method 

if __name__ == "__main__":                     # Standard Web Starter Instruction
    app = web.application(urls, globals())     # Mapping to line 4 'urls' variable to tell Python 
    app.run()                                  # Standard Web Starter Instruction

