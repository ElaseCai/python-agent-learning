'''class Steps:
    def __init__(self):
        self.steps=[{"step_number":1,"action" : "search","result": "Found 5 documents"},
            {"step_number":2,"action" : "open_document","result": "Document opened"},
            {"step_number":3,"action":"summarize","result" :"Summary generated"}]
    def get_action(self,step_num):
        return self.steps[step_num-1]["action"]
    def print_trajectory(self):
        for dic_i in self.steps:
            print("Step ",dic_i["step_number"],": ",dic_i["action"])

my_step=Steps()
try:
    my_step.get_action(5)
except IndexError:
    print("Out of scope!")
action=my_step.get_action(2)
print("The agent should perform:", action)
my_step.print_trajectory()

import json

with open("trajectory.json","r") as f:
    steps=json.load(f)

steps.append({
    "step": 4,
    "action": "finish",
    "result": "Task completed"
})

with open("trajectory.json","w") as f:
    json.dump(steps,f)


import requests
response=requests.post("https://httpbin.org/post",json={"name":"Alice","age":20})
data=response.json()
print(data["json"])


import requests
try:
    response=requests.get("https://httpbin.org/get")
    response.raise_for_status()
    data=response.json()
    print("success!")
except requests.exceptions.HTTPError:
    print("Request failed:",response.status_code)


import requests
print(requests.__version__)

from math_utils import multiply
print(multiply(3,4))

x=0
try:
    y=100/x
except ZeroDivisionError:
    print("division is 0")
else:
    print("Calculation successful!")
finally:
    print("This always runs!")
print("Program finished")

age=-5
try:
    if age<0:
        raise ValueError("Age cannot be negative!")
except ValueError:
    print("Invalid age!")
print("Program finished")
'''
import logging
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s | %(levelname)s | %(message)s")

class Step:
    def __init__(self):
        self.steps = [
            {"step": 1, "action": "search"},
            {"step": 2, "action": "open"},
            {"step": 3, "action": "summarize"}
            ]

    def get_action(self,step_num):
        try:
            if step_num<1:
                raise ValueError("Step number must be positive!")
            return self.steps[step_num-1]["action"]
        except IndexError:
            logging.exception("Step not found!")
        return None

a=Step()
print(a.get_action(2))
print(a.get_action(10))
try:
    print(a.get_action(0))
except ValueError:
    logging.exception("Invalid input!")
print("Program finished")