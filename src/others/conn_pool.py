import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from http.server import BaseHTTPRequestHandler

try:
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="pool",
                                                              pool_size=1,
                                                              pool_reset_session=True,
                                                              host='bayi',
                                                              database='upayprod',
                                                              user='admin',
                                                              password='password')
finally:
    print ('conn---:' , connection_pool)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    print ('test')