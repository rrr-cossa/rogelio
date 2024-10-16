# Initial list of student
#TODO: Create a List of student names. Add 10 names. Name this list as 'student'
student = ["Nico","Alheli","Sam", "Manfred","Dania","Pamela","Anahi","Quebec","Rogelio","Messi"]
def display_student():
    print(f"_____________________________________")
    print(f"Current student:\n")
    for i in student:
        print(i)

# Add a new student to the list
def add_student():
    new_name = input("Enter the new name: ")
    student.append(new_name)
    display_student()

# Remove a student from the list by name
def remove_student():
    remove = input("Remove an element from the list: ")
    if remove in student:
        student.remove(remove)
    if remove not in student:
        print("The element is not on the list")
    display_student()

# remove a student from the end of the list
def pop_student():
    if not student:
        print("There are no elements left")
    else:
        last = student.pop()
    print(f"{last} was removed from the end of the list")
    display_student()

# Update a student's name in the list
def update_student():
    name = input("Write the student name: ")
    if name in student:
        new = input("Write the name you want to update it for: ")
    find = student.index(name)
    student[find] = new
    if not new:
        print("This name does not exist")
    else:
        print("This name exist")
    display_student()

# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            pop_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            exit()
            break 

# Start the program
menu()