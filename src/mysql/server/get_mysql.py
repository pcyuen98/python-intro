import json

import web
from mysql.server.agent import Agent
from mysql.server.address import Address

URLS = (
    '/json/get', 'JsonGet'
)


class JsonGet(object):

    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        return get_agent()

def get_agent():
        agent = Agent()
        agent.fullName = "Testing"
        agent.contactNumber ="000"
        agent.email = "a.com"
        address = Address()
        address.fullAddress = "address";
        address.country = "MY"
        address.state = "1212"
        address.city = "KL"
        
        agent.address = address

        print ('agent ====' , agent.toJSON())
        return agent.toJSON()
        
def main():
    """
    Main function starting app
    """
    get_agent()
    http_app = web.application(URLS, globals())
    http_app.run()

if __name__ == "__main__":
    main()

