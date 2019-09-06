import numpy as np


class Product:
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=np.random.randint(1000000, high=9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        self.pw = self.price/self.weight
        if self.pw < 0.5:
            print('Not so stealable...')
        if (self.pw >= 0.5 and self.pw < 1):
            print('Kinda stealable.')
        else:
            print('Very stealable')

    def explode(self):
        self.fw = self.flammability*self.weight
        if self.fw < 10:
            print('...fizzle')
        if (self.fw >= 10 and self.fw < 50):
            print('...boom!')
        if (self.fw >= 50):
            print('...BABOOM!!!!')


class BoxingGlove(Product):
    def punch(self):
        if self.weight < 5:
            print('That tickles')
        if (self.weight >= 5 and self.weight < 15):
            print('Hey that hurt!')
        else:
            print('OUCH!')
