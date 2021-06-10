import csv





# Employee class code in Python

# Class definition
class Employee:

    def __init__(self, name, age, title, job_role, salary):
        self.__name = name
        self.age = age
        self.__title = title
        self._job_role = job_role
        self.salary = salary

# Getters & Setters
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getTitle(self) -> object:
        return self.__title

    def setTitle(self, title):
            self.__title = title


Sam = Employee("Sam", "27", "Mr", "Data Engineer", 100000)
Milan = Employee("Milan", "25", "Mr", "Data Engineer", 102000)
Tobi = Employee("Tobi", "26", "Mr", "Data Engineer", 103002)



Sam.setName("Samuel")
Sam.setTitle("Dr")
Milan.setTitle("Lord")
Milan.setName("Cosgrove")
Tobi.setTitle("King")


print(f"{Sam.getTitle()} {Sam.getName()} will see you now..")
print(f"{Milan.getTitle()} {Milan.getName()} will see you now..")
print(f"{Tobi.getTitle()} {Tobi.getName()} will see you now..")



