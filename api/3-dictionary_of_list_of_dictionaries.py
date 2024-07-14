#!/usr/bin/python3
"""Extending Task 0 to export data in
the JSON format from all task from
all employees"""


import requests # Imports from request module
import json # imports from json module


def employees_tasks():
    """Retrieve and export all TODO list tasks for all employees in JSON format"""
    # Initialize an empty dictionary to store tasks for all employees
    all_tasks = {}

    # Retrieve all users
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    # Iterate through each user and retrieve their TODO list
    for user in users:
        employee_id = user['id']
        todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()

        # Prepare tasks for the user
        user_tasks = []
        for task in todos:
            user_tasks.append({
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            })

        # Store tasks in the dictionary using user's ID as key
        all_tasks[employee_id] = user_tasks

    # Write all tasks to a JSON file
    with open("todo_all_employees.json", "w") as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    # Execute as the script. Retrieve and handle TODO lists for all employees
    employees_tasks()
