from random import randint


class Simulation(object):
    def __init__(self, players, total, start):
        self.players = players
        for x in players:
            x.shinies = start
        self.Shinies = total - (players * start)

    def iterate(self):
        FloatingValue = self.Shinies
        for x in self.players:
            Usage = randint(0, 5)
            x.shinies = x.shinies - Usage * (FloatingValue / 20)
            self.Shinies = self.Shinies - Usage * (FloatingValue / 20)

    def simulate(self, num):
        for x in num:
            self.iterate
            print self.Shinies
            for x in self.players:
                print x.shinies
