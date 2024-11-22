import json

def load_students(filename):
    students = {}
    with open(filename, 'r') as file:
        reader = json.load(file)
    for student_id, student_info in reader.items():
        student =  student_info[0]
        name = student["name"]
        grade = student["grade"]
        group = student["group"]

        students[student_id] = [name, grade, group]
    return students

def main():
    filename = 'data.json'
    students = load_students(filename)
    for student in students:
        print(f"Student ID: {student}")
        print(f"Name: {students[student][0]}")
        print(f"Grade: {students[student][1]}")
        print(f"Group: {students[student][2]}")
        print()

if __name__ == "__main__":
    main()