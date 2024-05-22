#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to
export data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json

"""

import json
import requests

if __name__ == "__main__":
    RESTAPI = "https://jsonplaceholder.typicode.com/users/"
    alldata = requests.get(RESTAPI)
    usersAll = alldata.json()
    usersDict = {}

    for user in usersAll:
        userID = user.get("id")
        un = user.get("username")
        url = RESTAPI + "{}".format(userID)
        url = url + "/todos"
        resp = requests.get(url)
        tasks = resp.json()
        usersDict[userID] = []
        for task in tasks:
            tasksComp = task.get("completed")
            tasksTitle = task.get("title")
            usersDict[userID].append(
                {"task": tasksTitle, "completed": tasksComp, "username": un}
            )
        with open("todo_all_employees.json", "w") as f:
            json.dump(usersDict, f)
