class Human:
    def __init__(self):
        self.name = ""
        self.age = ""

    def set_nameage(self,name,age):
        self.name = name
        self.age = age

    def printinfo(self):
        print(self.name)
        print(self.age)

human = Human()

human.set_nameage("侍太郎","35")
human.printinfo()