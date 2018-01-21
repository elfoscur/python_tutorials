class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):  # contructor, executed when the object is created
        print('I am constructed ', z)
        self.name = z

    def __del__(self):
        print('I am distructed ', self.name)

    def party(self):
        self.x = self.x + 1
        print(self.name,"So far ", self.x)


class FootballFan(PartyAnimal):  # FootballFan extends PartyAnimal, it shares the same methods and add new methods and datas
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)


an = PartyAnimal('pippo')  # an.x = 0 'pippo' will be passed in the parameter z

an.party()  # equivalent to PartyAnimal.party(an)
an.party()  # basically I'm passing the object as a parameter of method
PartyAnimal.party(an)  # print 3

an1 = PartyAnimal('pluto')
an1.party()

print(dir(PartyAnimal))  # returns methods and variables of the class
print(dir(an))  # do the same

an = 42  # it execute the __del__ method

j = FootballFan('Jim')  # execute the constructor of PartyAnimol
j.party()
j.touchdown()
