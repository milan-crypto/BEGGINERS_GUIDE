from Snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large= True
        self.two_lungs = True
        self.venom = False

Ola = Python()
Aaron = Python()
Aaron.large = False
print(Aaron.large)
print(Ola.large)


# This is Polymorphism

