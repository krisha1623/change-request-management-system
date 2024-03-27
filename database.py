import sqlite3

def connect_db():
    conn = sqlite3.connect('crmconn.db')
    cursor = conn.cursor()
    return conn, cursor

def close_db(conn, cursor):
    cursor.close()
    conn.close()

def create_table1():
    conn, cursor = connect_db()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS table1 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            request VARCHAR(300) NOT NULL,
            deadline DATETIME NOT NULL,
            time_of_request DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    close_db(conn, cursor)

def create_table2():
    conn, cursor = connect_db()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS table2 (
            id INTEGER PRIMARY KEY,
            code TEXT
        )
    ''')
    conn.commit()
    close_db(conn, cursor)

create_table1()
create_table2()