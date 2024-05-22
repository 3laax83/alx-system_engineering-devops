#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""

import json
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    urlUser = "https://jsonplaceholder.typicode.com/users/" + user
    res = requests.get(urlUser)
    userName = res.json().get("username")
    task = urlUser + "/todos"
    res = requests.get(task)
    tasks = res.json()

    dictData = {user: []}
    for task in tasks:
        compStatus = task.get("completed")
        taskTitle = task.get("title")
        dictData[user].append(
            {"task": taskTitle, "completed": compStatus, "username": userName}
        )
        with open("{}.json".format(user), "w") as f:
            json.dump(dictData, f)
