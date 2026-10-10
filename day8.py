import sqlite3
connection=sqlite3.connect("trajectory.db")
cursor=connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS steps(
    id      INTEGER PRIMARY KEY,
    step    INTEGER,
    action  TEXT,
    result  TEXT
    )
""")

cursor.execute("""
    INSERT INTO steps(step,action,result)
    VALUES(1,'search','found')
""")
cursor.execute("""
    INSERT INTO steps(step,action,result)
    VALUES(2,'create','success')
""")
connection.commit()

cursor.execute("""
    UPDATE steps
    SET result="failed"
    WHERE step=2
""")
connection.commit()

