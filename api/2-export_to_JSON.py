#!/usr/bin/python3
"""Extending Task 0 to export
data in the JSON format from all
tasks that are owned by this employee"""


import requests  # Imports from requests module
import sys  # Imports from sys module
import json  # Imports from json module


def todo_list(employee_id):
    """Retrieve and display the TODO list progress for an employee"""
    # Retrieve the user's data
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/"
                        f"{employee_id}").json()
    # Retrieve TODO list data
    todos = requests.get(f"https://jsonplaceholder.typicode.com/"
                         f"todos?userId={employee_id}").json()

    # Print the employee's TODO list
    print(f"Employee {user['name']} is done with tasks("
          f"{sum(task['completed'] for task in todos)}/{len(todos)}):")
    for task in todos:
        if task['completed']:
            print(f"\t {task['title']}")

    # Create JSON format for all tasks
    user_id = task["userId"]
    data = {
        employee_id: [
            {"task": task["title"],
             "completed": task["completed"],
             "username": user["username"]}
            for task in todos
        ]
    }

    # Write JSON to a file for the employee
    with open(f"{employee_id}.json", "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    # Execute the script
    todo_list(int(sys.argv[1]))
