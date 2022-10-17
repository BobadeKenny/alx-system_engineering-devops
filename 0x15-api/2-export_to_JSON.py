#!/usr/bin/python3
"""export api data to json"""
import json
import requests
import sys
if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    r = requests.get("{}/users/{}".format(url, id))
    user = r.json()
    r = requests.get("{}/todos?userId={}".format(url, id))
    todos = r.json()
with open("{}.json".format(id), "w") as file:
    json.dump({id: [{
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": user.get("username")} for task in todos]}, file)