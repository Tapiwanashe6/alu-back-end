import requests
import sys

def get_employee_todo_progress(employee_id):
    # URL for the API to get users and their todos
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    
    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found.")
        return
    
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch todos data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate completed tasks
    completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    # Display the result
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for employee ID.")
