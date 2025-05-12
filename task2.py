import json
import os

DATA_FILE = "students_data.json"
students = []

def load_data():
    global students
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                students = json.load(file)
            print("Previous student data loaded successfully.")
        else:
            print("No existing data file found. Starting with empty records.")
    except Exception as e:
        print(f"Error loading data: {e}")
        students = []

def save_data():
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(students, file, indent=4)
        print("Student data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

def display_student(student, index=None):
    if index is not None:
        print(f"\nStudent #{index + 1}")
    print(f"Name: {student['Name']}")
    print(f"Roll Number: {student['Roll_Number']}")
    print("Marks:")
    for subject, mark in student['Marks'].items():
        print(f"  {subject}: {mark}")

def display_all_students_details():
    print("\nAll Student Records")
    print("------------------")
    if not students:
        print("No student records found!")
        return
    
    for idx, student in enumerate(students):
        display_student(student, idx)
    print()

def validate_input(prompt, input_type="text", existing_rolls=None, subject=None):
    while True:
        try:
            value = input(prompt).strip()
            
            if not value:
                raise ValueError("Input cannot be empty")
            
            if input_type == "roll":
                if existing_rolls and value in existing_rolls:
                    raise ValueError("This roll number already exists")
                return value
            
            elif input_type == "mark":
                mark = int(value)
                if not 0 <= mark <= 100:
                    raise ValueError("Marks must be between 0 and 100")
                return mark
            
            elif input_type == "text":
                if not value.replace(" ", "").isalpha():
                    raise ValueError("Name should contain only letters and spaces")
                return value
            
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def add_student():
    existing_rolls = [s['Roll_Number'] for s in students]
    
    while True:
        print("\nAdd New Student")
        student = {
            'Name': validate_input("Enter Student Name: ", "text"),
            'Roll_Number': validate_input("Enter Roll Number: ", "roll", existing_rolls),
            'Marks': {
                'Maths': validate_input("Enter Maths marks (0-100): ", "mark"),
                'Physics': validate_input("Enter Physics marks (0-100): ", "mark"),
                'Chemistry': validate_input("Enter Chemistry marks (0-100): ", "mark")
            }
        }
        
        students.append(student)
        existing_rolls.append(student['Roll_Number'])
        print(f"\nStudent {student['Name']} added successfully!")
        
        if input("\nAdd another student? (y/n): ").lower() != 'y':
            break

def search_student():
    roll_mapping = {student['Roll_Number']: idx for idx, student in enumerate(students)}
    
    roll_no = validate_input("\nEnter Roll Number to search: ", "roll")
    if roll_no in roll_mapping:
        idx = roll_mapping[roll_no]
        print("\nStudent Found:")
        display_student(students[idx], idx)
        return idx
    else:
        print(f"\nNo student found with Roll Number: {roll_no}")
        return None

def edit_student():
    student_idx = search_student()
    if student_idx is None:
        return
    
    student = students[student_idx]
    print("\nEdit Student Details")
    
    if input(f"Edit name (current: {student['Name']})? (y/n): ").lower() == 'y':
        student['Name'] = validate_input("Enter new name: ", "text")
    
    for subject in student['Marks']:
        if input(f"Edit {subject} marks (current: {student['Marks'][subject]})? (y/n): ").lower() == 'y':
            student['Marks'][subject] = validate_input(f"Enter new {subject} marks (0-100): ", "mark")
    
    print("\nUpdated Student Details:")
    display_student(student, student_idx)

def main_menu():
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search/Edit Student")
    print("4. Save and Exit")

def get_menu_choice():
    while True:
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            print("Please enter a number between 1 and 4!")
        except ValueError:
            print("Invalid input! Please enter a number.")

def main():
    load_data()
    
    while True:
        main_menu()
        choice = get_menu_choice()
        
        if choice == 1:
            add_student()
        elif choice == 2:
            display_all_students_details()
        elif choice == 3:
            edit_student()
        elif choice == 4:
            save_data()
            print("\nExiting the program...")
            break

if __name__ == "__main__":
    main()