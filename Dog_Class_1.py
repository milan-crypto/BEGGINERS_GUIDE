class Dog:

    animal_kind = "Canine."

    def __init__(self, name, colour, age, breed):
        self.animal_kind = "Canine"
        self.name = name
        self.colour = colour
        self.age = age
        self.breed = breed
        self.bark()

    def bark(self):
        print("Woof!")

Amy = Dog("Amy", "Golden", "4 (Dog Years)", "Golden Retriever")


print(Amy.name)
print(Amy.colour)
print(Amy.age)
print(Amy.breed)



