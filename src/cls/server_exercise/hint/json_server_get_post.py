# This is to simulate the "POST" method from PostMan
from cls.server.json_server_method import JSONServerClass
JSONServerClass.setPerson('{"name":"Kiruban","address":"Selangor"}')

# This is to simulate the "GET" method from PostMan
print('value inside memory------------->' , JSONServerClass.getPerson())
