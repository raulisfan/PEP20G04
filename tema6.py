class Fabrica():

    contor1 = 0
    contor2 = 0

    def __init__(self, inceput:int, ziua:int, n:int, track = {}):


        self.inceput = inceput
        self.ziua = ziua
        self.n = n
        self.track = track
        self.t = inceput

    def adauga(self):

        while self.contor1 < self.n:

            self.track[self.contor1] = [self.ziua, self.inceput, self.inceput//20]
            self.inceput += 1
            self.contor1 += 1

        return self.track

    def rightside(self):


        for a, b, c in self.track.values():
            if c % 2 == 1:
                print(c, end=',')

    def leftside(self):

        for a, b, c in self.track.values():
            if c % 2 == 0:
                print(c, end=',')

    def __iter__(self):
        return self

    def __next__(self):

        if self.contor2 > self.n:
            raise StopIteration

        rezultat = self.inceput // 20

        self.t += 1
        self.contor2 += 1

        return rezultat

prima = Fabrica(111, 10, 91)
print(prima.adauga())

print('rightside:')
prima.rightside()
print()

print('\nleftside:')
prima.leftside()
print()

file = open('text', mode='w')

for x in prima:
    file.write(str(x))
    file.write('\n')

file.close()
print()