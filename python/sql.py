import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

# Create the table if not already exists
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""

cursor.execute(table_info)

# Insert some records (only if table is empty to avoid duplicates)
cursor.execute("SELECT COUNT(*) FROM STUDENT")
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute('''INSERT INTO STUDENT VALUES('Manish','Data science','A',90)''')
    cursor.execute('''INSERT INTO STUDENT VALUES('Krish','Data science','A',90)''')
    cursor.execute('''INSERT INTO STUDENT VALUES('Sudhanshu','Data science','B',86)''')
    cursor.execute('''INSERT INTO STUDENT VALUES('Darius','Data science','A',86)''')
    cursor.execute('''INSERT INTO STUDENT VALUES('Vikash','DEVOPS','A',50)''')
    cursor.execute('''INSERT INTO STUDENT VALUES('Dipesh','DEVOPS','A',35)''')

# Display all the records
print("The rows in STUDENT table are:")
data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()
