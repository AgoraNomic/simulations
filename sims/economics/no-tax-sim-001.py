from random import randint


class Simulation(object):
    def __init__(self, players, total, start):
        self.players = players
        for x in players:
            global x.shinies
            x.shinies = start
        self.Shinies = total - (players * start)

    def iterate(self):
        FloatingValue = self.Shinies
        for x in self.players:
            global x.shinies
            Usage = randint(0, 5)
            x.shinies = x.shinies - Usage * (FloatingValue / 20)
            self.Shinies = self.Shinies - Usage * (FloatingValue / 20)
        for x in floor(self.players / 3):
            global x.shinies
            x.shinies = x.shinies + 10
            self.Shinies = self.Shinies - 10

    def simulate(self, num):
        for x in num:
            self.iterate
            print self.Shinies
            for x in self.players:
                global x.shinies
                print x.shinies


A = Simulation(15, 1000, 50)
A.simulate(5)
