# Python + Flask API

This is an API that hosts test stubs for future MyPass services. It is written in Python & Flask. 

# Running the example

First, be sure to set up a virtual environment:

```bash
virtualenv venv
source venv/bin/activate
``` 


1. Install the needed dependencies with `pip3 install -r requirements.txt`
2. Start the server with `python3 server.py`
3. Try calling [http://localhost:3010/test-api/test-type/<test_id>](http://localhost:3010/)
 #Try it out
 
 once the is server is running try sending an image file via the curl command

```bash 
curl http://0.0.0.0:3010/test-api/bio/openhand.jpg
``` 

This is just a framework.  In a real test, the api endpoint would match an actual REST api

TODO: add AUTH0 to the server