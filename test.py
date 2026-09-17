import psycopg2
def table():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Mihir@1907", host="localhost",port="5433" )

    cursor =conn.cursor()
    cursor.execute('''create table employees(Name text, ID int, Age int);''')
    print('Table created Successfully')

    conn.commit()
    conn.close()

def data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Mihir@1907", host="localhost",port="5433" )

    cursor =conn.cursor()

    name = input('Enter your name: ')
    id = int(input('Enter your ID: '))
    age = int(input('Enter your Age: '))

    query = '''insert into employees(Name, ID, Age) values(%s, %s, %s);'''
    values = (name, id, age)
    cursor.execute(query, values)
    print('Data inserted Successfully')

    conn.commit()
    conn.close()
data()

def extract():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Mihir@1907", host="localhost",port="5433")
    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    print(cursor.fetchall())
    conn.commit()
    conn.close()
extract()

def update():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Mihir@1907", host="localhost",port="5433" )
    cursor =conn.cursor()   
    id = int(input('Enter your ID to update: '))
    age = int(input('Enter your new Age: '))
    query = '''update employees set Age=%s where ID=%s;'''
    values = (age, id)
    cursor.execute(query, values)
    print('Data updated Successfully')
    conn.commit()
    conn.close()
update()
