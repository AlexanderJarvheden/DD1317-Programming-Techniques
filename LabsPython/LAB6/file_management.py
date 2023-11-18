import os
from person import Student, Teacher
import error_handling

def enter_valid_file(school):
    """Makes the user enter valid file, print all people in the file, and store them to the school class"""
    while True:
        filename = input("Vad heter filen med alla personer? ")
        if os.path.exists(filename):
            with open(filename, 'r') as file:   # Open the file to read
                lines = file.readlines()    # Read all the lines
                print(f"\nDessa personer är skrivna på {school.name}\n")
                # Go through the lines, one at a time and split it into right format
                for i in range(0, len(lines), 4):   # Split to read 4 lines at a time (Ssn, prename, surname, role)
                    ssn = lines[i].strip()
                    last_name = lines[i + 1].strip()
                    first_name = lines[i + 2].strip()
                    role = lines[i + 3].strip()
                    if role == "student":
                        student = Student(f"{first_name} {last_name}", str(ssn))
                        school.students.append(student)
                        school.all_people.append(student)
                        ssn = student.ssn
                    if role == "lärare":
                        teacher = Teacher(f"{first_name} {last_name}", str(ssn))
                        school.teachers.append(teacher)
                        school.all_people.append(teacher)
                        ssn = teacher.ssn
                    print(f"Namn: {first_name} {last_name} Personnr: ", str(ssn))
            return
        else: 
            print("Den filen fanns inte! Skriv in en ny fil: ")

def search_people_in_file():
    """Search if the search criteria exists in the file"""
    while True:
        filename = input("Vad heter filen med alla personer? ")
        search_criteria = error_handling.enter_valid_search()
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
                # Go through the lines, one at a time and split it into right format
                for i in range(0, len(lines), 4):
                    ssn = lines[i].strip()
                    last_name = lines[i + 1].strip()
                    first_name = lines[i + 2].strip()
                    if search_criteria in (first_name, last_name, ssn):
                        print(f"Namn: {first_name} {last_name} Personnr: ", str(ssn))                
                return
        else: 
            print("Den filen fanns inte! Skriv in en ny fil: ")

