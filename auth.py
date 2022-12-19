from flask import *
import cx_Oracle
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/register_db', methods= ['GET','POST'])
def register_db():
    First_Name = request.form['firstName']
    LastName = request.form['lastName']
    Email = request.form['email']
    Phone = request.form['phone']
    Password = request.form["password"]
    path = 'system/sys@//localhost:1521/xe'
    cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_21_7")
    connection = cx_Oracle.connect(path) 
    cursor = connection.cursor()
    try:
        cursor.execute("create table Register (first_name varchar(50),last_name varchar(50),email_id varchar(100),phone number(10),password varchar(10))")
    
    except:
        print("table present")
    cursor.execute("""select FIRST_NAME,EMAIL_ID from Register where FIRST_NAME = :first_name and EMAIL_ID = :email""",first_name = First_Name, email = Email )
    isAvailable = False
    for i in cursor.fetchmany():
        if i[0] == First_Name and i[1] == Email:
            isAvailable = True
    if isAvailable == False :
        cursor.execute("""insert into Register values(:firstname, :lastname, :email, :phone, :password)""",firstname = First_Name,lastname = LastName, email = Email, phone = Phone, password = Password )
        connection.commit()
        
        return render_template('Index.html')
    else:
        return "you have already register"


@app.route('/login')
def login():
    return render_template('login.html')
       
   

@app.route('/login_db',methods = ['POST','GET'])
def login_db():
    Login_Email = request.form["login_email"]
    Login_Password = request.form["login_password"]
    path = 'system/sys@//localhost:1521/xe'
    client_path=cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_21_7-20221215T235126Z-001\instantclient_21_7")
    connection = cx_Oracle.connect(path) 
    cursor = connection.cursor()
    try:
        cursor.execute("create table Login (email_id varchar(100),password_ varchar(10),date_time varchar2(100))")
    except:
        print("table present")

    connection.commit()
    cursor.execute("""select EMAIL_ID,PASSWORD from Register where  EMAIL_ID = :email and PASSWORD = :password """,email = Login_Email, password = Login_Password ) 
    isAvailable = False
    for i in cursor.fetchmany():
        if i[0] == Login_Email and i[1] == Login_Password:
                Date_Times = datetime.now()
                Date_Time = Date_Times.strftime("%d/%m/%Y %H:%M:%S")
                cursor.execute("""insert into Login values(:email,:password,:date_time)""",email = Login_Email, password = Login_Password ,date_time = Date_Time)
                connection.commit()
                isAvailable = True
                return render_template('userdashboard.html')
    if isAvailable == False:
        return 'password is wrong'

@app.route('/userdash', methods=['POST','GET'])
def userdash():
    return render_template('userdashboard.html')

@app.route('/userdashboard_db', methods= ['POST','GET'])
def userdashboard_db():
    User_Name = request.form['user_name']
    Age = request.form['age']
    LawyerName=request.form['lawyer_name']
    LawyerAddr=request.form['lawyer_addr']
    LawyerContact=request.form['lawyer_contact']
    path = 'system/sys@//localhost:1521/xe'

    client_path=True
    if client_path==False:
        client_path=cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_21_7-20221215T235126Z-001\instantclient_21_7")
    connection = cx_Oracle.connect(path) 
    cursor = connection.cursor()
    try:
        cursor.execute("create table Booking_App1 (user_name varchar(20),age number(10),lawyer_name varchar(10),lawyer_addr varchar(100), lawyer_contact(10)")
    
    except:
        print("table present")

    connection.commit()
    cursor.execute("""select user_name, age from Booking_App1 where user_name = :user_name and age= :age""",user_name = User_Name, age= Age )
    isAvailable = False
    
    cursor.execute("""insert into Booking_App1 values(:username, :age, :lawyername, :lawyeraddr, :lawyercontact)""",username = User_Name, age=Age,lawyername =LawyerName, lawyeraddr=LawyerAddr, lawyercontact=LawyerContact)

    isAvailable=True
    connection.commit()
    return render_template('userdashboard.html')
    path = 'system/sys@//localhost:1521/xe'
    cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_21_7")
    connection = cx_Oracle.connect(path) 
    cursor = connection.cursor()
    cursor.execute("""select FIRST_NAME from Register """)

    if isAvailable==False:
        return 'Time slot is booked for Appointment, please select other time'
    
    


    
       
if __name__ == '__main__':
    app.run(debug = True)