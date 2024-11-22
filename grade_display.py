import tkinter as tk

def display_grade():
    grade = grade_entry.get().upper()
    if grade == "O":
        grade_description = "Outstanding"
    elif grade == "A":
        grade_description = "Very Good"
    elif grade == "B":
        grade_description = "Good"
    elif grade == "C":
        grade_description = "Average"
    elif grade == "F":
        grade_description = "Fail"
    else:
        grade_description = "Not valid"

    label2.config(text=grade_description)
    
root = tk.Tk()
root.title("Grades Display GUI")
root.geometry("400x400")

instruction_label = tk.Label(root, text="Enter Grade (O, A, B, C, F):")
instruction_label.pack()

grade_entry = tk.Entry(root, width=10)
grade_entry.pack()

submit_button = tk.Button(root, text="Submit", command=display_grade)
submit_button.pack()

label2 = tk.Label(root, text="")
label2.pack()

root.mainloop()