class Dog:

    def __init__(self,character, spotted):
        self.wicked_kind = character
        self.coloring = spotted

    def sit (self):
        print("give the command to the dog to sit")

    def to_lie(self):
        print("give the command to the dog to lie down")

    def voice(self):
        print("give the dog a voice command")

    def __str__(self):
        return "I'm dog"

class Labrador(Dog):
    def __init__(self, character,spotted,weight):
        super().__init__(character,spotted)
        self.weight = weight

    def sit(self):
        print("the dog did not follow the command to sit")

    with open('../file_name') as file:
        pass

class GermanShepherd(Dog):
    def __init__(self,character = 'obedient',spotted = 'black_yellow' ):
        super().__init__(character,spotted)

    def coup(self):
        print("German Shepherd made the team coup")

    def overlook(self):
        print("you lost sight of your German Shepherd")

copy1 = Dog("character", "spotted")
copy2 = Labrador("character", "spotted", 16)
copy3 = GermanShepherd()
big_dog = GermanShepherd()