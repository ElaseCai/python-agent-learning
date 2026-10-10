import argparse
import sqlite3
import database
parser=argparse.ArgumentParser()# 创建一个参数解析器
sub1=parser.add_subparsers(dest="command")
add_parser=sub1.add_parser("add")
add_parser.add_argument("step",type=int)
add_parser.add_argument("action")
add_parser.add_argument("result")
list_parser=sub1.add_parser("list")
delete_parser=sub1.add_parser("delete")
delete_parser.add_argument("step_id",type=int)
arg=parser.parse_args()#真正读取并解析参数 

connection=sqlite3.connect("trajectory.db")
database.create_table(connection)

if arg.command=="add":
    database.add_step(connection,arg.step,arg.action,arg.result)
elif arg.command=="list":
    print(database.get_steps(connection))
elif arg.command=="delete":
    database.delete_step(connection,arg.step_id)

'''
parser.add_argument("command")#告诉解析器参数规则
parser.add_argument("step", type=int)
arg=parser.parse_args()#真正读取并解析参数 
print(arg.command)
print(arg.step)
print(type(arg.step))
'''