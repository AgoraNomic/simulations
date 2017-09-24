from random import randint
from math import floor


class Simulation(object):
    def __init__(self, players, total, start):
        global x
        self.players = players
        for x in players:
            x = start
        self.Shinies = total - (players * start)

    def iterate(self):
        global x
        FloatingValue = self.Shinies
        for x in self.players:
            Usage = randint(0, 5)
            x = x - Usage * (FloatingValue / 20)
            self.Shinies = self.Shinies - Usage * (FloatingValue / 20)
        for x in floor(self.players / 3):
            x = x + 10
            self.Shinies = self.Shinies - 10

    def simulate(self, num):
        for x in num:
            self.iterate
            print(self.Shinies)
            for x in self.players:
                print(x)


A = Simulation(15, 1000, 50)
A.simulate(5)
