# PostgreSQL Database Operations using Python

## Project Overview

This project demonstrates how to connect Python with a PostgreSQL database and perform basic database operations such as creating a table, inserting records, and retrieving data using the `psycopg2` library.

## Features

* Connects to a PostgreSQL database
* Creates a table named `class`
* Inserts student records into the database
* Retrieves and displays all records
* Uses exception handling for database operations

## Technologies Used

* Python 3.x
* PostgreSQL
* psycopg2

## Prerequisites

Before running the project, ensure you have:

1. Python 3.x installed
2. PostgreSQL installed and running
3. psycopg2 package installed

Install psycopg2 using:

```bash
pip install psycopg2
```

## Database Configuration

Update the database credentials in the Python file if necessary:

```python
dbname = "postgres"
user = "postgres"
password = "your_password"
host = "localhost"
port = "5433"
```

## Project Structure

```text
Project Folder/
│
├── Task1.py
└── README.md
```

## How to Run the Project

1. Start the PostgreSQL server.
2. Verify the database connection details in the code.
3. Open a terminal in the project directory.
4. Execute the program:

```bash
python Task1.py
```

## Program Workflow

### 1. Create Table

The program creates a table named `class` with the following fields:

| Column Name | Data Type |
| ----------- | --------- |
| Name        | VARCHAR   |
| Rollno      | INTEGER   |
| Division    | VARCHAR   |
| House       | VARCHAR   |

### 2. Insert Records

The user is prompted to enter:

* Student Name
* Roll Number
* Division
* House

The entered data is stored in the PostgreSQL database.

### 3. Display Records

All records stored in the `class` table are fetched and displayed.

## Sample Output

```text
Enter Name: Mihir
Enter Roll Number: 101
Enter Division: A
Enter House: Red

Record inserted successfully.

('Mihir', 101, 'A', 'Red')
```

## Learning Outcomes

Through this project, you will learn:

* Database connectivity in Python
* SQL table creation
* Data insertion using SQL queries
* Data retrieval from PostgreSQL
* Exception handling in database applications

## Author

Mihir Mendake

