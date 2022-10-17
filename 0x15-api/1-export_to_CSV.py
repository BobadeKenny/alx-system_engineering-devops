#!/usr/bin/python3
"""export api data to csv"""
import csv
import requests
import sys
if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    r = requests.get("{}/users/{}".format(url, id))
    user = r.json()
    r = requests.get("{}/todos?userId={}".format(url, id))
    todos = r.json()
    with open("{}.csv".format(id), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow([user.get('id'), user.get('username'),
                                task.get('completed'),
                                task.get('title')])
