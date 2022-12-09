from src import create_app
from flask import Flask
#from flask_restful import Api, Resource

app = Flask(__name__)
#api = Api(app)


app = create_app()


# Start our server and Flask application 
# Only in developing environment we will use this for the debug logs
if __name__ =='__main__':
    app.run(debug=True)
    
    