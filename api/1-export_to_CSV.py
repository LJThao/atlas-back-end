#!/usr/bin/python3
"""Extending Task 0 to export data in
CSV format"""


import csv  # Imports from csv module
import requests  # Imports from requests module
import sys  # Imports from sys module


def todo_list(employee_id):
    """Retrieving and displaying the TODO list for an employee"""
    # Retrieve the employee's data
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/"
                        f"{employee_id}").json()
    # Retrieve the TODO list data
    todos = requests.get(f"https://jsonplaceholder.typicode.com/"
                         f"todos?userId={employee_id}").json()

    # Print the employee's TODO list
    print(f"Employee {user['name']} is done with tasks("
          f"{sum(task['completed'] for task in todos)}/{len(todos)}):")
    for task in todos:
        if task['completed']:
            print(f"\t {task['title']}")

    # Writing tasks to a CSV file
    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id,
                             user['name'],
                             task['completed'],
                             task['title']])


if __name__ == "__main__":
    # Execute the script
    todo_list(int(sys.argv[1]))
