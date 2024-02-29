import web

urls = (
     '/', 'RootURL'    # the RootURL is mapping to the class name below on line 9

)

class RootURL:
    def GET(self):
        print ('helo')

if __name__ == "__main__":                     # Standard Web Starter Instruction
    app = web.application(urls, globals())     # Mapping to line 4 'urls' variable to tell Python 
    app.run()                                  # Standard Web Starter Instruction

