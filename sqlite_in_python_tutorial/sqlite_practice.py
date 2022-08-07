import sqlite3

#conn = sqlite3.connect('customers.db')

#c = conn.cursor()

# Creating the Table:
#c.execute("""CREATE TABLE customers(
    #first_name text,
    #last_name text,
    #e_mail text)""")

# Inserting a Single Record into the Database
'''
c.execute("INSERT INTO customers VALUES ('Mary', 'Blow', 'mb@test.com')")

# Inserting multiple records at once:
many_customers = [
    ('Hermione', 'Granger', 'hg@hogwarts.com'),
    ('Ronald', 'Weesley', 'rw@hogwarts.com'),
    ('Harry', 'Potter', "hp@hogwarts.com")
]

c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)
'''

# Querying the Database
#c.execute("SELECT * FROM customers")
#c.execute("SELECT rowid, * FROM customers")
#c.execute("SELECT * FROM customers WHERE last_name = 'Granger'")
#c.execute("SELECT * FROM customers WHERE last_name LIKE 'Wee%'")
#c.execute("SELECT * FROM customers WHERE e_mail LIKE '%hogwarts.com'")
#print(c.fetchone()) # fetch one
#c.fetchmany(2) # fetch two 
#print(c.fetchall()) # fetch all

# How do we update records ...?
#c.execute("""UPDATE customers SET first_name = 'Joe'
 #           WHERE rowid=1
  #          """)
#conn.commit()

# How do we delete records ...?
#c.execute("DELETE from customers WHERE rowid = 1")

#c.execute("SELECT rowid, * FROM customers")
#c.execute("SELECT rowid, * FROM customers")


#print("NAME " + "\t\tEMAIL")
#print("----" + "\t\t-----" )
#for item in items:
    #print(item[0] + " " + item[1] + " " + item[2])

# Ordering Results
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
'''
# AND/OR:
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Po%' OR rowid = 4")
items = c.fetchall()
for item in items:
    print(item)
'''

# Limiting Results returned:
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")
#items = c.fetchall()
#for item in items:
    #print(item)

# Deleting a Table:
#c.execute("DROP TABLE customers")

# Our App: Show All Function--Query the Database and Return All Records
def show_all():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    
    for item in items:
        print(item)

    conn.commit()
    conn.close()

# Add a new record to the table:
def add_one(first_name, last_name, email):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first_name, last_name, email))
    conn.commit()
    conn.close()

# To delete a row, rowid needs to be passed as a string, NOT an integer
def delete_one(id):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()
    print(f"Record with id# {id} has been deleted.")

def add_many(list):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", (list))
    conn.commit()
    conn.close()
    print(f"Record with id# {id} has been added.")

def email_lookup(email):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers WHERE e_mail = (?)", (email,))
    items = c.fetchall()
    
    for item in items:
        print(item)
    conn.commit()
    conn.close()
    


# Searching for Specific Things
#print("Commands executed successfully ...")
#conn.commit()
#conn.close()


