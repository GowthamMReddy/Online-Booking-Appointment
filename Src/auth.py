from flask import *
import cx_Oracle



app = Flask(__name__)

@app.route('/Register', methods= ['GET','POST'])
def Register():
    First_Name = request.form['firstName']
    LastName = request.form['lastName']
    Email = request.form['email']
    Phone = request.form['phone']
    Password = request.form["password"]


    
    path = 'system/sys@//localhost:1521/xe'
    cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_21_7")
    connection = cx_Oracle.connect(path) 
    cursor = connection.cursor()
    cursor.execute("""insert into Register values(:firstname, :lastname, :email, :phone, :password)""",firstname = First_Name,lastname = LastName, email = Email, phone = Phone, password = Password )
    connection.commit()
    if request.method == 'POST':
         return ' HELLO %s'%First_Name

    else:
        return 'erroe'


@app.route('/Login', methods = ['POST','GET'])
def Login():
    Email = request.form['login_email']
    Password = request.form['login_password']
    path = 'system/sys@//localhost:1521/xe'
    cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_21_7")
    connection = cx_Oracle.connect(path) 
    cursor = connection.cursor()
    cursor.execute("""insert into Login values(:email, :password)""",email = Email , password = Password )
    connection.commit()
    if request.method == 'POST':
         return ' HELLO %s'%Email

    else:
        return 'erroe'





if __name__ == '__main__':
    app.run(debug = True)
