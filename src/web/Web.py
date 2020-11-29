import web

urls = (
     '/', 'index1'    # the index1 is mapping to the class name below on line 4

)

class index1:
    def GET(self):
        import GetWebMethod                  # import something from GetMethod py File
        #return "Hello Chrome 123!"        # return simple message
        return GetWebMethod.sparePart()   # return GetMethod PY file and Spare Part Method 

if __name__ == "__main__":                     # Standard Web Starter Instruction
    app = web.application(urls, globals())     # Mapping to line 4 'urls' variable to tell Python 
    app.run()                                  # Standard Web Starter Instruction

