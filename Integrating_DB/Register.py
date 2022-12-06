import cx_Oracle 

path = "system/sys@//localhost/xe"
cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_21_7")
with cx_Oracle.connect(path) as connection:
    cursor = connection.cursor()
    cursor.execute("create table Register__ (first_name varchar(10),last_name varchar(10),emil_id varchar(10),phone number(10),password varchar(10))")
    print(cursor.fetchmany())