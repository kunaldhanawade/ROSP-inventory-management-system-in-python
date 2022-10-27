import sqlite3
def create_db():
    con=sqlite3.connect(database=r'inventorymanagementsystem.db')
    cur=con.cursor()

    # ========employee table ==============

    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,utype text,salary text)")
    con.commit() 

    # =========product table =============

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,name text,price text,qty text,status text)")
    con.commit() 
    
create_db()