from Reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        print("Do I smell nice? Or do I taste nice?")


Oscar = Snake()
Oscar.use_tongue_to_smell()

# This is Encapsulation