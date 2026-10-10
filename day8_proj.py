'''
你需要：

import json
打开 trajectory.json
json.load() 读取
把结果存到变量 data
print(data)
'''
import json
import sqlite3
with open("trajectory.json","r") as f:
    data=json.load(f)
print(data)

connect=sqlite3.connect("trajectory.db")
cursor=connect.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS steps(
    id      INTEGER PRIMARY KEY,
    step    INTEGER,
    action  TEXT,
    result  TEXT
    )
""")
for i in data:
    a=i["step"]
    b=i["action"]
    c=i["result"]
    cursor.execute("""
        INSERT INTO steps(step,action,result)
        VALUES (?,?,?)
    """,(a,b,c))
connect.commit()

cursor.execute("""
    SELECT *
    FROM steps
""")
print(cursor.fetchall())