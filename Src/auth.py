from flask import *
import cx_Oracle



app = Flask(__name__)

@app.route('/home', methods= ['GET','POST'])
def home():
    First_Name = request.form['firstName']
    path = 'system/sys@//localhost/xe'
    cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_21_7")
    connection = cx_Oracle.connect(path) 
    cursor = connection.cursor()
    cursor.execute("""insert into login__ values(:dep, :dep1)""",dep=First_Name,dep1='lihkth')
    connection.commit()


        
    if request.method == 'POST':
         return ' HELLO %s'%First_Name

    else:
        return 'erroe'

 

if __name__ == '__main__':
    app.run(debug = True)
