#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    employee = ''
    taskComplete = 0
    arrayTask = []
    tasks = 0
    apiPage = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])

    query = requests.get(apiPage)
    employee = query.json['name']
    pagID = ("https://jsonplaceholder.typicode.com/todos?userId={}".format
             (argv[1]))
    query = requests.get(pagID)
    for task in query.json():
        tasks += 1
        if task.get('completed') is True:
            taskComplete += 1
            arrayTask.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(employee,
                                                          task_complete,
                                                          tasks))

    for task in arrayTask:
        print("\t", task)
