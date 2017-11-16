from mysql.connector import connect

#CREATE DATABASE cinemas_db;

def connect_to_cin_db():
    cnx = connect(user="root", password="cnxpass",
                  host="127.0.0.1", database="cinemas_db")
    print("Połączenie udane.")
    return cnx

create_Cinema_sql = """CREATE TABLE Cinema (
id int AUTO_INCREMENT,
name varchar(255),
address TEXT,
PRIMARY KEY(id)
)"""

create_Movie_sql = """CREATE TABLE Movie (
id int AUTO_INCREMENT,
name varchar(255),
description TEXT,
PRIMARY KEY(id)
)"""

create_Ticket_sql = """CREATE TABLE Ticket (
id int AUTO_INCREMENT,
quantity int,
price FLOAT(5,2),
PRIMARY KEY(id)
)"""

create_Payment_sql = """CREATE TABLE Payment (
id int AUTO_INCREMENT,
type varchar(255),
data DATE,
PRIMARY KEY(id)
)"""

if __name__ == '__main__':
    conn = connect_to_cin_db()
    cursor = conn.cursor()
    cursor.execute(create_Cinema_sql)
    cursor.execute(create_Movie_sql)
    cursor.execute(create_Ticket_sql)
    cursor.execute(create_Payment_sql)

    cursor.close()
    conn.close()

