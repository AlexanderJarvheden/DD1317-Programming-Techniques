class Person:
    """Creates people with name and social security number"""

    def __init__(self, name, ssn):  
        """"Initialize a new person with name and social security number"""
        self.name = name
        self.ssn = ssn

    def __str__(self):
        """"Format the person as its name and social security number"""
        return f"Namn: {self.name} Personnr: {self.ssn}"
    
class Student(Person):
    """A class for creating students"""
    def work(self):
        """Returns the role"""
        return "Student"
    
class Teacher(Person):
    """A class for creating Teachers"""
    def work(self):
        """Returns the role"""
        return "Teacher"