def ask_names():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    full_name = first_name + last_name
    count = len(full_name)
    
    initials = f"{first_name[0]}{last_name[0]}"
    
    double_first_name = ''
    for i in first_name:
        double_first_name += i * 2
        
    last_name_backward = last_name[::-1]
    
    print(f"Hello {first_name}, {last_name}! Your name has {count} letters, and your initials are {initials}.")
    print(f"{double_first_name}, your last name spelled backwards is {last_name_backward}.")

ask_names()