# A class is a blueprint. Like an unfilled questionnaire.

class Dog:

    animal_kind = "Dog."  # class variable which returns an attribute string.

    def bark(self):  # method (basically a function but when inside a class it is called a method).
        return "Woof!"


Myles = Dog()
Oscar = Dog()

# print(type(Myles))
# print(type(Oscar))
# print(Myles.animal_kind)
# print(Oscar.animal_kind)
print(Myles.bark())
print(Oscar.bark())

Oscar.animal_kind = "Big Dog."
print(Myles.animal_kind)
print(Oscar.animal_kind)



