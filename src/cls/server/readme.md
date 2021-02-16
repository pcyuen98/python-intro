# requirement to test
1. postman https://www.postman.com/
2. python web.py

run the web.py server from json_server

available API as below

# add object 
http://localhost:8080/post

{
   "name":"Kap",
   "address":" An Address"
}


# get objects
http://localhost:8080/get

# search name object
http://localhost:8080/search?name=Kap