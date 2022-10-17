#!/usr/bin/python3
"""for a given employee ID, returns
information about his/her TODO list progress."""
import requests
import sys
if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    r = requests.get("{}/users/{}".format(url, id))
    user = r.json()
    r = requests.get("{}/todos?userId={}".format(url, id))
    todos = r.json()
    completed_tasks = []
    for task in todos:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task))
