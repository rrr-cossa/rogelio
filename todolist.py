# A simple to-do list manager for high school students using functions and list comprehension

# Initial to-do list
todo_list = ["Math homework", "Science project", "Read history book", "Practice piano"]

# Function to display the current to-do list
def display_todo_list():
    #TODO display the list
    print("Write your to do list: ")
    print(todo_list)
    
# Function to add a new task
def add_task(task):
    #TODO the user wants to add a task. 
    new_todo = input("Write a new thing you would like to do: ")
    todo_list.append(new_todo)
    
# Function to remove a task by its name
def remove_task(task):
    #TODO 
    remove_todo = input ("Enter the element you would like to remove from the to do list: ")
    if remove_todo in todo_list:
        todo_list.remove(remove_todo)
    else:
        print("Error")
        
# Function to find the index of a task
def find_task(task):
    #The user wants to know in what position is a task. 
    task = input("Task the element you would like to find")
    print(todo_list.index(task))
    
# Function to complete and remove the first task
def complete_task():
    #The user wants to remove the first task. 
    todo_list.pop(0)
    print("First task removed")
    
# Function to filter tasks containing a specific keyword using list comprehension
def filter_tasks(keyword):
    #TODO create a list comprehension variable to filter tasks containing a specific keyword
    keyword = input("Write a keyword to find the task: ")
    filtered_tasks = [task for task in todo_list if keyword in task]
    print(f"\nTasks containing '{keyword}':")
    print(filtered_tasks if filtered_tasks else "No tasks found.")

# Main menu to choose options
def main():
    while True:
        print("\nTo-Do List Manager Menu")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Find Task")
        print("5. Complete First Task")
        print("6. Filter Tasks by Keyword")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")

        #TODO create the if staments for the user. 
        if choice == "1":
            display_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            find_task()
        elif choice == "5":
            complete_task()
        elif choice == "6":
            filter_tasks()
        elif choice == "7":
            break

# Run the main function
main()

