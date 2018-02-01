import psycopg2

def create_table():
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' "
                            "host = 'localhost' port = '5432' ")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' "
                            "host = 'localhost' port = '5432' ")
    cursor = conn.cursor()
    #cursor.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    cursor.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

#insert("Water Glass", 10, 5)

def view():
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' "
                            "host = 'localhost' port = '5432' ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' "
                            "host = 'localhost' port = '5432' ")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item = %s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' "
                            "host = 'localhost' port = '5432' ")
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()

create_table()
#insert("Orange", 10, 15)

update(11, 6, "Orange")
delete("Apple")
print(view())