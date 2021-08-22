# Dev Assessment - Webhook Receiver
## Setup
* Create a new virtual environment
  ``` pip install virtualenv ```
* Create the virtual env 
  ``` python3 -m venv env ```
* Activate the virtual env
  ``` source env/bin/activate ```
* Install Requirements 
  ``` pip install -r requirements.txt ```
* Run the flask application 
  ``` python3 run.py ```
* The endpoint is at:
  ``` POST http://127.0.0.1:5000/ ```
* Use ngrok to expose ip to internet
  ``` ./ngrok http 5000 ```
