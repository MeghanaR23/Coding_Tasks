import json
import os

DATA_FILE = "students_data.json"

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks if marks is not None else {} 
    
    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)
    
    def to_dict(self):
        return {
            'Name': self.name,
            'Roll_Number': self.roll_number,
            'Marks': self.marks
        }

students = []

def load_data():
    global students
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                student_dicts = json.load(file)
                students = []
                for s in student_dicts:
                    students.append(Student(s['Name'], s['Roll_Number'], s['Marks']))
            print("Previous student data loaded successfully.")
        else:
            print("No existing data file found. Starting with empty records.")
    except Exception as e:
        print(f"Error loading data: {e}")
        students = []

def save_data():
    try:
        student_dicts = []
        for student in students:
            student_dicts.append(student.to_dict())
        
        with open(DATA_FILE, 'w') as file:
            json.dump(student_dicts, file, indent=4)
        print("Student data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

def display_student(student, index=None):
    if index is not None:
        print(f"\nStudent #{index + 1}")
    print(f"Name: {student.name}")
    print(f"Roll Number: {student.roll_number}")
    print("Marks:")
    for subject, mark in student.marks.items():
        print(f"  {subject}: {mark}")
    print(f"Average Marks: {student.average():.2f}")

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
    existing_rolls = [s.roll_number for s in students]
    
    while True:
        print("\nAdd New Student")
        name = validate_input("Enter Student Name: ", "text")
        roll_number = validate_input("Enter Roll Number: ", "roll", existing_rolls)
        marks = {
            'Maths': validate_input("Enter Maths marks (0-100): ", "mark"),
            'Physics': validate_input("Enter Physics marks (0-100): ", "mark"),
            'Chemistry': validate_input("Enter Chemistry marks (0-100): ", "mark")
        }
        
        student = Student(name, roll_number, marks)
        students.append(student)
        existing_rolls.append(roll_number)
        print(f"\nStudent {student.name} added successfully!")
        
        if input("\nAdd another student? (y/n): ").lower() != 'y':
            break

def search_student():
    roll_no = validate_input("\nEnter Roll Number to search: ", "roll")
    for idx, student in enumerate(students):
        if student.roll_number == roll_no:
            print("\nStudent Found:")
            display_student(student, idx)
            return idx
    print(f"\nNo student found with Roll Number: {roll_no}")
    return None

def main_menu():
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Save and Exit")

def get_menu_choice():
    """Get and validate menu choice"""
    while True:
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            print("Please enter a number between 1 and 5!")
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
            search_student()
        elif choice == 4:
            save_data()
            print("\nExiting the program...")
            break

if __name__ == "__main__":
    main()