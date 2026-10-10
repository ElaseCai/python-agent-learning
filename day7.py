import logging
handler1=logging.FileHandler("app.log",mode="w")
handler1.setLevel(logging.DEBUG)
handler2=logging.StreamHandler()
handler2.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s | %(levelname)s | %(message)s",handlers=[handler1,handler2])
'''logging.debug("This is a debug message")
logging.info("Program started")
logging.warning("Something may be wrong")
logging.error("Something went wrong")

def get_user():
    return {"name": "Alice", "age": 20}

user = get_user()
logging.debug("user = %s",user)
name = user["name"]

print(name)
'''
try:
    10 / 0
except ZeroDivisionError:
    logging.error("division is 0!")