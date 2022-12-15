
from flask import Flask
from views import views
from src import create_app
#from flask_restful import Api, Resource

app = Flask(__name__)
#api = Api(app)
app.register_blueprint(views, url_prefix="/")

# Start our server and Flask application 
# Only in developing environment we will use this for the debug logs

if __name__=='__main__':
    app.run(debug=True)
app = create_app()


    
    
