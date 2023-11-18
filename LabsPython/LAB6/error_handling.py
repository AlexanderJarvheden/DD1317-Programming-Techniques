
def translate_usr_choice(usr_choice):
    """Translates the user choice of one letter to full words, used in future print statements"""
    if usr_choice == "l":
        return "lägga till"
    elif usr_choice == "a":
        return "ändra"
    elif usr_choice == "s":
        return "söka"
    else:
        return "ta bort"


def validate_usr_choice():
    """Validates that the input actually is a possible choice"""
    while True:
        usr_choice = input(
            "\nVill du lägga till (l), ändra (a), ta bort (t) eller söka (s) efter en person på skolan? "
        )
        if usr_choice in ("l", "a", "t", "s"):  # Check if the input is one of the parameters
            formated_usr_choice = translate_usr_choice(
                usr_choice
            )  # Turn input into right format (extend letter to words)
            return formated_usr_choice
        else:
            print("Du måste mata in enligt formatet l, a, t eller s. Försök igen!")


def enter_valid_role():
    """Validates that the user creates a person with an existing role"""
    while True:
        role = input("Vad för roll har personen?\n")
        print("\n")
        if role == "student":
            return "student"
        elif role == "lärare":
            return "lärare"
        print("Personen måste vara lärare eller student, försök igen")


def enter_valid_ssn(choice):
    """Validates that the ssn only contains integers, and returns it as a string to enable the first integer to be a zero"""
    while True:
        try:
            ssn = input(
                f"Skriv in personnumret på personen du vill {choice}: "
            )  # Choice depends on "lägga till", "ändra" or "ta bort"
            control_format = int(ssn)
            return ssn
        except ValueError:
            print("Personnumret får bara innehålla siffror, försök igen!")

def enter_valid_search():
    """Make sure that the search is valid"""
    while True:    
        search_criteria = input("Vill du söka efter förnamn (f), efternamn (e) eller personnummer (p)?")
        if search_criteria == "f":
            return input("Vad heter personen i förnamn? ")
        elif search_criteria == "e":
            return input("Vad heter personen i efternamn? ")
        elif search_criteria == "p":
            return input("Vilket är personens personnummer? ")
        else:
            print("Du skrev fel, försök igen...")