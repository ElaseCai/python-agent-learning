import sqlite3
def create_table(connection):
    cursor=connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS steps(
        id INTEGER PRIMARY KEY,
        step INTEGER,
        action TEXT,
        result TEXT
        )
    """)
    connection.commit()

def add_step(connection, step, action, result):
    cursor=connection.cursor()
    cursor.execute("""
        INSERT INTO steps(step, action, result)
        VALUES(?,?,?)
    """,(step, action, result))
    connection.commit()
    return cursor.lastrowid

def get_steps(connection):
    cursor=connection.cursor()
    cursor.execute("""
        SELECT *
        FROM steps
    """)
    return cursor.fetchall()

def get_step(connection, step_id):
    cursor=connection.cursor()
    cursor.execute("""
        SELECT *                  
        FROM steps
        WHERE id=?
    """,(step_id,))
    return cursor.fetchone()

def update_step(connection, step_id, result):
    cursor=connection.cursor()
    cursor.execute("""
        UPDATE steps
        SET result=?
        WHERE id=?
    """,(result,step_id))
    connection.commit()

def delete_step(connection, step_id):
    cursor=connection.cursor()
    cursor.execute("""
        DELETE FROM steps
        WHERE id=?
    """,(step_id,))
    connection.commit()
    