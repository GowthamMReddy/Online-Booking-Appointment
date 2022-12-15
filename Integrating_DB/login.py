import cx_Oracle

path = "system/sys@//localhost/xe"
cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_21_7")
with cx_Oracle.connect(path) as connection:
    cursor = connection.cursor()
    cursor.execute("create table Login (email_id varchar(100),password_ varchar(10))")
    
    
    
