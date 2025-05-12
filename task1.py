
Students = []
num_of_students = int(input("How many students data you wish to enter?"))
for i in range(num_of_students):
    Student_details = {}
    Marks = {}
    Student_Name = input("Enter the Student Name:")
    Roll_Num = input("Enter the Roll Number:")

    Maths = int(input("Enter the Marks of the Maths: "))
    Physics = int(input("Enter the Marks of the Phsyics: "))
    Chemistry = int(input("Enter the Marks of the Chemistry: "))

    Marks.update({'Maths':Maths,'Physics':Physics,'Chemistry':Chemistry})
    Student_details.update({'Name':Student_Name,'Roll Number':Roll_Num,'Marks':Marks})

    Students.append(Student_details)

print("\n")    
print("Students_Details:")
for student in Students:
    print(f"Name:{student['Name']}")
    print(f"Roll Number:{student['Roll Number']}")
    print("Marks:")
    for subject, mark in student['Marks'].items():
        print(f"{subject}:{mark}")
    print("\n")