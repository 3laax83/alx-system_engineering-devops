#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.CSV
"""

import csv
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

    with open("{}.csv".format(user), "w") as csvFile:
        for task in tasks:
            comp = task.get("completed")
            titleTask = task.get("title")
            csvFile.write(
                '"{}","{}","{}","{}"\n'.format(user, userName, comp, titleTask)
            )
