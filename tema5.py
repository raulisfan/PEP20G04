from math import cos, acos

class Triangle():

    def __init__(self, A = 1, B = 1, C = 1, AB = 60, BC = 60, CA = 60):
        self.A = A
        self.B = B
        self.C = C
        self.AB = AB
        self.BC = BC
        self.CA = CA

    def modify_angle(self, degree, angle):
        try:
            if angle == 'BC':
                self.BC = self.BC + degree

                self.A = (self.B * 2 + self.C * 2 - 2 * self.B * self.C * cos(self.BC)) ** (1 / 2)

                self.AB = acos((self.A * 2 + self.B * 2 - self.C ** 2) / (2 * self.A * self.B))
                self.CA = acos((self.C * 2 + self.A * 2 - self.B ** 2) / (2 * self.C * self.A))

                if self.BC > 180 or self.BC < 0 or self.AB > 180 or self.AB < 0 or self.CA > 180 or self.CA < 0:
                    raise Exception

            elif angle == 'AB':
                self.AB = self.AB + degree

                self.C = (self.A * 2 + self.B * 2 - 2 * self.A * self.B * cos(self.AB)) ** (1 / 2)

                self.BC = acos((self.B * 2 + self.C * 2 - self.A ** 2) / (2 * self.B * self.C))
                self.CA = acos((self.C * 2 + self.A * 2 - self.B ** 2) / (2 * self.C * self.A))

                if self.BC > 180 or self.BC < 0 or self.AB > 180 or self.AB < 0 or self.CA > 180 or self.CA < 0:
                    raise Exception

            elif angle == 'CA':
                self.CA = self.CA + degree

                self.B = (self.C * 2 + self.A * 2 - 2 * self.C * self.A * cos(self.CA)) ** (1 / 2)

                self.AB = acos((self.A * 2 + self.B * 2 - self.C ** 2) / (2 * self.A * self.B))
                self.BC = acos((self.B * 2 + self.C * 2 - self.A ** 2) / (2 * self.B * self.C))

                if self.BC > 180 or self.BC < 0 or self.AB > 180 or self.AB < 0 or self.CA > 180 or self.CA < 0:
                    raise Exception

            else:
                print('gresit')

        except Exception as e:
            print('nu e interval (0,180)')

    def modify_side(self, meters, side):
        try:
            if side == 'B':
                self.B = self.B + meters

                self.A = ((self.B + meters) / self.B) * self.A
                self.C = ((self.B + meters) / self.B) * self.C

                if self.A + self.C <= self.B:
                    raise Exception
            elif side == 'A':
                self.A = self.A + meters

                self.B = ((self.A + meters) / self.A) * self.B
                self.C = ((self.A + meters) / self.A) * self.C

                if self.B + self.C <= self.A :
                    raise Exception
            elif side == 'C':
                self.C = self.C + meters

                self.A = ((self.C + meters) / self.C) * self.A
                self.B = ((self.C + meters) / self.C) * self.B

                if self.B + self.A <= self.C:
                    raise Exception

            else:
                print('gresit')

        except Exception as e:
            print('')

triunghi = Triangle()

triunghi.modify_angle('AB', 30)
triunghi.modify_side('A', 1.5)

print(triunghi.AB)
print(triunghi.A)