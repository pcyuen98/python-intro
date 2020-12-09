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

import web
import json

URLS = (
    '/', 'HandleIndex',
    '/json/(.*)', 'HandleJSON'
)

# Only for testing purpose. Do not use in production!
LAST_JSON_DOC = 'No JSON document.'


class HandleIndex(object):

    def GET(self):
        """
        Callback method handling HTTP GET request
        """
        return LAST_JSON_DOC


class HandleJSON(object):

    def POST(self, res):
        """
        Callback method handling HTTP POST request
        """
        global LAST_JSON_DOC
        json_data = web.data()
        LAST_JSON_DOC = json.loads(json_data)
        print ('data received ====' , LAST_JSON_DOC)
        return LAST_JSON_DOC


def main():
    """
    Main function starting app
    """
    http_app = web.application(URLS, globals())
    http_app.run()


if __name__ == "__main__":
    main()
