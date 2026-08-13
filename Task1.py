import psycopg2

def table():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Mihir@1907",host="localhost", port="5433")
    
    cursor = conn.cursor()

    cursor.execute('''create table class(Name text, Rollno int, Division text, House text)''')
    print("Table created successfully")

    conn.commit()
    conn.close()

def insert():
    # Insert data into the table
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Mihir@1907",host="localhost", port="5433")
    cursor = conn.cursor()

    Name = str(input("Enter Name: "))
    Rollno = int(input("Enter Roll Number: "))
    Division = str(input("Enter Division: "))
    House = str(input("Enter House: "))

    query = '''insert into class(Name, Rollno, Division, House) values(%s, %s, %s, %s)'''
    values = (Name, Rollno, Division, House)
    cursor.execute(query, values)
    print("Data inserted successfully")

    conn.commit()
    conn.close()

def extract():
      conn = psycopg2.connect(dbname="postgres", user="postgres", password="Mihir@1907", host="localhost",port="5433" )
      cursor =conn.cursor()   
      cursor.execute('''select * from class;''')
      print(cursor.fetchall())
      conn.commit()
      conn.close()
extract()