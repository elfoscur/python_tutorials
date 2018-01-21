class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far ", self.x)


an = PartyAnimal()  # an.x = 0

an.party()  # equivalent to PartyAnimal.party(an)
an.party()  # basically I'm passing the object as a parameter of method
PartyAnimal.party(an)  # print 3
