import database
import sqlite3
import argparse
import logging
parser=argparse.ArgumentParser()
sub_parser=parser.add_subparsers(dest="command")
list_parser=sub_parser.add_parser("list")
add_parser=sub_parser.add_parser("add")
add_parser.add_argument("step",type=int)
add_parser.add_argument("action")
add_parser.add_argument("result")
show_parser=sub_parser.add_parser("show")
show_parser.add_argument("step_id",type=int)
delete_parser=sub_parser.add_parser("delete")
delete_parser.add_argument("step_id",type=int)
arg=parser.parse_args()

connect=sqlite3.connect("trajectory.db")
database.create_table(connect)

if arg.command=="list":
    print(database.get_steps(connect))
elif arg.command=="add":
    id=database.add_step(connect,arg.step,arg.action,arg.result)
    print(id)
elif arg.command=="show":
    result=database.get_step(connect,arg.step_id)
    if result is None:
        print("ID not valid")
    else:
        print(result)
elif arg.command=="delete":
    result=database.get_step(connect,arg.step_id)
    if result is None:
        print("ID not valid")
    else:
        database.delete_step(connect,arg.step_id)
        print("Step deleted successfully")
