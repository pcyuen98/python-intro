
import json
import sys

import web

from agent.server.address import Address
from agent.server.agent import Agent
import pymysql as MySQLdb
from agent.server.user import User
from agent.server.email_client import AgentEmail
from agent.server.donate import Donate


sys.path.append('../')
sys.path.append('../../')

URLS = (
    '/json/get', 'JsonGet',
    '/json/getUser', 'JsonGetUser',
    '/json/post', 'JsonPost',
    '/register/post', 'CreatePost',
    '/donate/post', 'DonatePost',
)

class DonatePost(object):

    def POST(self):
        
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Methods', 'content-type');
        print('CreatePost starting' )

        json_data = web.data()
        
        donate = Donate.setUser(json_data)
        print('donate-->' , donate )
        print('donate email-->' , donate.email )
        # need to convert to List Object to Json String else Angular cannot process it 
        user_id = createDonateDB(donate)
        return user_id
        
        #return jsonString
    def OPTIONS(self):
        
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Access-Control-Allow-Methods', 'content-type');
        print('OPTIONS starting' )
        
class CreatePost(object):

    def POST(self):
        
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        
        print('CreatePost starting' )

        json_data = web.data()
        
        user = User.setUser(json_data)
        print('user-->' , user )
        print('user email-->' , user.email )
        # need to convert to List Object to Json String else Angular cannot process it 
        user_id = createUserDB(user)
        return user_id
        
        #return jsonString
    def OPTIONS(self):
        
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        
        print('OPTIONS starting' )
        
class JsonPost(object):

    def POST(self):
        
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        
        print('JsonPost starting' )

        json_data = web.data()
        
        agent = Agent.setAgent(json_data)
        print('agent-->' , agent )
        # need to convert to List Object to Json String else Angular cannot process it 
        insertDB(agent)
        
        #return jsonString
    def OPTIONS(self):
        
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        
        print('OPTIONS starting' )
        

class Redirect(object):

    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        print ('here')
        user_input = web.input()

        
class JsonGet(object):

    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        user_input = web.input()
        return get_agent_db(user_input.id)
    
class JsonGetUser(object):

    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        user_input = web.input()
        return get_user_db(user_input.id)
    
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

def get_agent_db(id):
    
    
    conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
    cursor = conn.cursor()
    sql = "select * from agent where agent_id = " + str(id);
    print ('sql->', sql)
    cursor.execute(sql)
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    myresult = cursor.fetchall()

    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    agent_json = json.dumps(json_data[0])
    
    agent = json.loads(agent_json)
    address_json = get_address_db(agent['address_id'])
    agent['address'] = json.loads(address_json)
    print ('json_str-->' , json.dumps(agent))
    return json.dumps(agent)

def get_user_db(id):
    
    conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
    cursor = conn.cursor()
    sql = "select * from user where user_id = " + str(id);
    print ('sql->', sql)
    cursor.execute(sql)
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    myresult = cursor.fetchall()

    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    user_json = json.dumps(json_data[0])
    
    user = json.loads(user_json)
    print ('user -->' , user)

    return user_json

def get_address_db(address_id):
    conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
    cursor = conn.cursor()

    cursor.execute("select * from address where address_id=" + str(address_id))
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    myresult = cursor.fetchall()
    #print('myresult-->', myresult)
    #for x in myresult:
     #   print(x)

    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    json_str = json.dumps(json_data[0])
    return json_str

def createDonateDB(donate: Donate):
    try:
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()
        print ('donate.email---->' + donate.email)
        print ('donate.email str---->' + str(donate.email))
        mySql_insert_query = """INSERT INTO donate (`email`) 
                           VALUES (%s) """
        donate: Donate
        record = (str(donate.email))
        print ('mySql_insert_query->', mySql_insert_query)
        cursor.execute(mySql_insert_query, record)

        conn.commit()
        user_id = cursor.lastrowid
        print('user_id-->' , user_id)

        return user_id

    except conn.Error as error:
        print (cursor._executed)
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        print (cursor._executed)
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
        
def createUserDB(user: User):
    try:
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()
        print ('user.email---->' + user.email)
        print ('user.email str---->' + str(user.email))
        mySql_insert_query = """INSERT INTO user (`email`) 
                           VALUES (%s) """
        user: User
        record = (str(user.email))
        print ('mySql_insert_query->', mySql_insert_query)
        cursor.execute(mySql_insert_query, record)

        conn.commit()
        user_id = cursor.lastrowid
        print('user_id-->' , user_id)

        AgentEmail().register_email(user.email, user_id)
        return user_id

    except conn.Error as error:
        print (cursor._executed)
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        print (cursor._executed)
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
        
def insertDB(agent: Agent):
    try:
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()

        mySql_insert_query = """INSERT INTO address (`fullAddress`, `country`, `state`, `city`) 
                           VALUES (%s, %s, %s, %s) """
        address: Address
        address = agent.address
        
        record = (address.fullAddress, address.country, address.state, address.city)
        print ('mySql_insert_query->', mySql_insert_query)
        cursor.execute(mySql_insert_query, record)

        conn.commit()
        address_id = cursor.lastrowid
        print('address_id-->' , address_id)

        mySql_insert_query = """INSERT INTO agent (`fullName`, `contactNumber`, `email`,`gpsURL`,`address_id`, `url`, `desc`, `user_id`) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
                           
        record = (agent.fullName, agent.contactNumber, agent.email, agent.gpsUrl, address_id, agent.url, agent.desc, agent.user_id)

        cursor.execute(mySql_insert_query, record)
        print (cursor._executed)
        conn.commit()

        agent_id = cursor.lastrowid
        print('agent_id-->' , agent_id)
        
        user = get_user_db(agent.user_id)
        wjdata = json.loads(user)
        print('email->' + wjdata["email"]);

        AgentEmail().send_email(wjdata["email"], agent_id, agent.fullName)

    except conn.Error as error:
        print (cursor._executed)
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        print (cursor._executed)
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
            
def main():
    """
    Main function starting app
    """
    print (sys.path)
    from cheroot.server import HTTPServer
    from cheroot.ssl.builtin import BuiltinSSLAdapter
    
    ssl_cert = 'cert.crt'
    ssl_key = 'key.key'

    HTTPServer.ssl_adapter = BuiltinSSLAdapter(certificate=ssl_cert,private_key=ssl_key)

    #get_agent()
    #user = User()
    #user.email = 'pcyuen98@gmail.com'
    #user_id = createUserDB(user)

    #print ('user_id-->' , str(user_id))
    http_app = web.application(URLS, globals())
    http_app.run()
if __name__ == "__main__":
    main()

