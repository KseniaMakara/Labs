class TRTriangle():
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, value):
        if value >= 0:
            self.__a = value
        else:
            raise Exception('a should be positive')
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, value):
        if value >= 0:
            self.__b = value
        else:
            raise Exception('a should be positive')
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, value):
        if value >= 0:
            self.__c = value
        else:
            raise Exception('c should be positive')
    def print_a_b_c(self):
        self.a = float(input(' Enter first side = '))
        self.b = float(input(' Enter second side = '))
        self.c = float(input(' Enter third side = '))
        print(' First side is {0}, second side is {1}, third side is {2}'.format(self.a,self.b,self.c))
    def print_perimeter(self):
        p = self.a+self.b + self.c
        print(p)
    def square(self):
        p = self.a + self.b + self.c
        h_p = p/2
        s = (h_p(h_p-self.a)(h_p-self.b)(h_p-self.c))**1/2
        print(s)
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
        return (other.a + self.a, other.b + self.b, other.c + self.c)

    def __sub__(self, other):
        return (other.a - self.a, other.b - self.b, other.c - self.c)

    def __mul__(self, other):
        return (other * self.a, other * self.b, other * self.c)

class TPiramid(TRTriangle):
    def __init__(self, a=0, b=0, c=0, h=0):
        super().__init__(a, b, c)
        self.h = h

    def print_h(self):
        self.h = float(input('Enter hight = '))
        return self.h

    def v(self):
        return super().square() * self.h/3

#______________________________________
t = TRTriangle()
t.print_a_b_c()
t.print_perimeter()
t.square()
pyramid=TPiramid(TRTriangle)
pyramid.print_h()
pyramid.v()








