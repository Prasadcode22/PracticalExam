import sqlite3
def create_table():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS employees
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  age INTEGER NOT NULL,
                  position TEXT NOT NULL)''')

    conn.commit()
    conn.close()

def insert_record(name, age, position):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    c.execute('''INSERT INTO employees (name, age, position)
                 VALUES (?, ?, ?)''', (name, age, position))

    conn.commit()
    conn.close()

def delete_record_by_position(position):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    c.execute('''DELETE FROM employees WHERE position=?''', (position,))

    conn.commit()
    conn.close()

# Create the table
create_table()

# Insert records
insert_record('John Doe', 30, 'Manager')
insert_record('Jane Smith', 25, 'Engineer')

# Delete records
delete_record_by_position('Manager')

# Print all records
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

c.execute('''SELECT * FROM employees''')
records = c.fetchall()

for record in records:
    print(record)

conn.close()
