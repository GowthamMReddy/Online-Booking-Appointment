
from flask import Flask
from Src import create_webapp
app= create_webapp()

if __name__=='__main__':
    app.run(debug=True, port=8000)