import sys
command=sys.argv[1]
if command=="add":
    try:
        step=int(sys.argv[2])
        action=sys.argv[3]
        result=sys.argv[4]
        print("Adding step ",step)
        print("Action: ",action)
        print("Result: ",result)
    except IndexError:
        print("Missing arguments")
    except ValueError:
        print("Step must be an integer")
elif command=="list":
    print("Listing...")
elif command=="delete":
    print("Deleting...")
else:
    print("Unknown command")

