from flask.helpers import make_response
from techstax import *
from techstax import create_app

app = create_app()

if __name__=='__main__':
    app.run(debug=True)