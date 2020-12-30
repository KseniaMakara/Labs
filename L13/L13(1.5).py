class TRTriangle():
    def __init__(self, a=0):
        self.a = a
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, value):
        if value >= 0:
            self.__a = value
        else:
            raise Exception('a should be positive')
    def print_a(self):
        self.a = float(input(' Enter first side = '))
        print(self.a)
    def print_perimeter(self):
        return 3*self.a
    def square(self):
        p = self.a*3
        h_p = p/2
        return self.a*3**(1/3)/4

    def __lt__(self, other):
        return self.square()<other.square()

    def __eq__(self, other):
        return self.square() == other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __add__(self, other):
        return TRTriangle(other.a + self.a)

    def __sub__(self, other):
        return TRTriangle(self.a - other.a)

    def __mul__(self, other):
        return TRTriangle(other * self.a)

class TPiramid(TRTriangle):
    def __init__(self, a=0, h=0):
        super().__init__(a)
        self.h = h

    def __add__(self, other):
        return TPiramid(other.a + self.a, self.h + other.h)

    def __sub__(self, other):
        return TPiramid(self.a - other.a, self.h - other.h )

    def __mul__(self, other):
        return TPiramid(other * self.a, other*self.h)

    def print_h(self):
        self.h = float(input('Enter hight = '))
        print(self.h)

    def square(self):
        p = self.a*3
        h_p = p/2
        l = float(input('enter l='))
        return self.square()+l*self.print_perimeter()/2

    def v(self):
        return super().square() * self.h/3


#______________________________________
t = TRTriangle()
t.print_a()
t.print_perimeter()
t.square()
pyramid=TPiramid()
pyramid.print_h()
pyramid.v()
