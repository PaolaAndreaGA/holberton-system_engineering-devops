#!/usr/bin/python3
""" Python3 REST API example EXPORT to csv"""
import csv
import requests
import sys


if __name__ == '__main__':

    id_employee = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/" + id_employee
    res = requests.get(url_user).json()
    username = res.get("username")
    req = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (id_employee) + '/todos')
    with open("{}.csv".format(sys.argv[1]), "w") as file_csv:
        writer = csv.writer(file_csv, quoting=csv.QUOTE_ALL)
        for task in req.json():
            writer.writerow([id_employee, username,
                             task.get("completed"), task.get("title")])
