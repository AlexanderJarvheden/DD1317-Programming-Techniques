from person import Student, Teacher
import error_handling


class School():
    """Class that is a school containing students, teachers, and keeps track of all people"""
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.all_people = []    # Keeps track of all the people in the school

    def add_person(self):
        """Adds a person as a student or teacher to the school"""
        title = error_handling.enter_valid_role()
        name = input("Vad heter personen?\n")
        ssn = error_handling.enter_valid_ssn("lägga till")
        if title == "student":
            student = Student(name, ssn)    # Instanciate a student
            self.students.append(student)   # Add to list of students
            self.all_people.append(student) # Add to list of people in the school
            print("\nPersonen tillagd\n")
        elif title == "lärare":
            teacher = Teacher(name, ssn)
            self.teachers.append(teacher)
            self.all_people.append(teacher)
            print("\nPersonen tillagd\n")
    
    def change_person_name(self):
        """Changes the name of a person in the school"""
        ssn = error_handling.enter_valid_ssn("ändra")
        for person in self.all_people:
            if person.ssn == ssn:
                while True:
                    usr_choice = input(f"Vill du ändra namn på {person.name} (j/n)? ")
                    if usr_choice == "j":
                        old_name = (person.name)  # Store old name to be used in print statement
                        new_name = input("Skriv in det nya namnet: ")
                        person.name = new_name
                        print(f"\nNu är namnet för {old_name} ändrat till {person.name}!\n")
                        return
                    elif usr_choice == "n":
                        print(f"{person.name} ändrar inte sitt namn!\n")
                        return
                    else:
                        print("Du måste svara j eller n annars blir det felformaterat...")
        print(f"Det finns tyvärr ingen person med personnumret {ssn}\n")

    def delete_person(self):
        """Deletes a person from its role list, and all people list"""
        ssn = error_handling.enter_valid_ssn("ta bort")
        for person in self.all_people:
            if person.ssn == ssn:
                while True:
                    usr_choice = input(f"Vill du ta bort {person.name} (j/n)? ")
                    if usr_choice == "j":
                        role = person.work()
                        if role == "Student":
                            self.students.remove(person)    # Remove from student list and all people
                            self.all_people.remove(person)
                            print(f"{person.name} togs bort från listan!\n")
                            return
                        elif role == "Teacher":
                            self.teachers.remove(person)
                            self.all_people.remove(person)
                            print(f"{person.name} togs bort från listan!\n")
                            return
                        
                    elif usr_choice == "n":
                        print(f"{person.name} tas inte bort från listan!\n")
                        return
                    else:
                        print("Du måste svara j eller n annars blir det felformaterat...")
        print(f"Det finns tyvärr ingen student med personnumret {ssn}\n")  # If no student was found, tell the user that the ssn doesn't exist

    def print_all_people(self):
        """Prints all people in the school"""
        print(f"Här är alla studenter på {self.name}")
        for student in self.students:
            print(student)
        print(f"\n\nHär är alla lärare på {self.name}")
        for teacher in self.teachers:
            print(teacher)

def search_people(self):
    """Search for people in the school"""
    while True:
        search_choice = input("\nVad vill du söka efter? Namn (n) eller personnummer (p)? ")
        if search_choice == "n":
            search_name = input("Vad heter personen du söker efter (för- och efternamn)? ")
            for student in self.students:
                if student.name == search_name:
                    print(f"\nStudenten {search_name} läser på {self.name}:\n")
                    print(student)
            for teacher in self.teachers:
                if teacher.name == search_name:
                    print(f"Läraren {search_name} undervisar på {self.name}:\n")
                    print(teacher)
            return
        elif search_choice == "p":
            search_ssn = input("Vad heter personen du söker efter (för- och efternamn)? ")
            for student in self.students:
                if student.ssn == search_ssn:
                    print(f"\nStudenten med personnumret {search_ssn} som läser på {self.name} är:")
                    print(student)
                else: 
                    print(f"Det finns ingen student på {self.name} med personnummer {search_ssn}")
            for teacher in self.teachers:
                if teacher.name == search_name:
                    print(f"\Läraren med personnumret {search_ssn} som undervisar på {self.name} är:")
                    print(teacher)
                else:
                    print(f"Det finns ingen lärare på {self.name} med personnummer {search_ssn}")
            return
        else:
            print("Du skrev fel, försök igen.")