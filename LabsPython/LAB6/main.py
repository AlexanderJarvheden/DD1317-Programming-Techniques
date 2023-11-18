import error_handling
from school import School
import file_management

def main():
    school_name = input("Vad heter skolan?\n")  # Name the school
    school = School(school_name)
    file_management.enter_valid_file(school)    # Print all people from the file
    while True:
        choosen_option = error_handling.validate_usr_choice()  # User will choose which action to do
        if choosen_option == "söka":
            file_management.search_people_in_file()
        else:
            num_of_executions = int(
                input(f"Hur många personer vill du {choosen_option}? ")
            )
            if choosen_option == "lägga till":
                for i in range(num_of_executions):
                    school.add_person()
                school.print_all_people()
            elif choosen_option == "ta bort":
                while num_of_executions > 0 and len(school.all_people) > 0:
                    school.delete_person()
                    num_of_executions -= 1  # Decrement since we have done one execution
                if num_of_executions > 0:   # If user wants more deletions but list is empty, notify the user
                    print(f"Kan inte ta bort {num_of_executions} till, listan är tom...")
            
            else:
                while num_of_executions > 0 and len(school.all_people) > 0:
                    school.change_person_name()
                    num_of_executions -= 1  # Decrement since we have done one execution
                if len(school.all_people) == 0:
                    print("Listan är tom, finns inga personer att ändra")


if __name__ == "__main__":
    main()