#!/usr/bin/python3
"""A Python script that uses a REST
API, for a given employee ID, returns
information about his/her TODO list"""


import requests # Importing from requests module so it can handle HTTP requests
import sys # Importing from sys module so it can handle command-line arguments


def todo_list(employee_id):
    """Retrieving the TODO list for an employee and returns the information"""
    # Retrieve the employee's data from the API and then converts it to JSON
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    # Retrieve the TODO list data for the employee and then converts it to JSON
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()

    # Print the employee's TODO list in this format
    print(f"Employee {user['name']} is done with tasks({sum(task['completed'] for task in todos)}/{len(todos)}):")
    # Loop through the tasks and then print the titles of the completed tasks
    for task in todos:
        if task['completed']: # Checks if the task is completed
            print(f"\t {task['title']}") # Print a tab and space before the title 


if __name__ == "__main__":
    # Execute the script, access the first command-line argument, and convert the ID to an integer
    todo_list(int(sys.argv[1]))
