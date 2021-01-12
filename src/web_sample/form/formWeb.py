"""
This module tries to print JSON from HTTP GET/POST method.
"""


#
# To test the application run application with:
#
# python ./webpy_json.py
#
# and type following URI in browser addres bar:
#
# http://localhost:8080/json/{"name": "Joe"}
#


URLS = (
    '/', 'handleIndex',
    '/json/(.*)', 'handleJSON'
)

# Only for testing purpose. Do not use in production!
LAST_JSON_DOC = 'No JSON document.'


class handleIndex(object):

    def GET(self):
        """
        Callback method handling HTTP GET request
        """
        return LAST_JSON_DOC


class handleJSON(object):

    def POST(self, req):
        """
        Callback method handling HTTP POST request
        """
        global LAST_JSON_DOC
        import web
        json_data = web.data()
        import json
        LAST_JSON_DOC = json.loads(json_data)
        print ('data received ====' , LAST_JSON_DOC)
        return LAST_JSON_DOC


def main():
    """
    Main function starting app
    """
    import web 
    http_app = web.application(URLS, globals())
    http_app.run()


if __name__ == "__main__":
    main()
