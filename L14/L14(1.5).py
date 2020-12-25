import random
class TTriangle():
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
class ETriangle(TTriangle):
    def __init__(self, a):
        super().__init__(a)
    def square(self):
        sq = (self.a**2*3**1/2)/4
        return sq

class ITriangle(TTriangle):
    def __init__(self, a, b ):
        super().__init__(a,b)
        self.a = float(input(' Enter first side = '))
        self.b = float(input(' Enter second side = '))
        print(a,a,b)
    def print_perimeter(self):
        p = 3*self.a
        print(p)

class RTriangle():
    def __init__(self, a=0, b=0):
        super().__init__(a, b)
    def print_a_b_c(self):
        self.a = float(input(' Enter first side = '))
        self.b = float(input(' Enter second side = '))
        c = (self.a ** 2 + self.b ** 2) ** 1 / 2
        print(' First side is {0}, second side is {1}, third side is {2}'.format(self.a,self.b, c))
    def square(self):
        ss = self.a*self.b/2
        return ss

t1 = ETriangle(3)
t2 = ETriangle(6)
t3 = RTriangle(5,6)
t4 = RTriangle(6,7)
t5 = ITriangle(4,3)
t6 = ITriangle(7,9)

tt=t1
tt.square()
tt=t2
tt.square()
tt=t3
tt.square()
tt=t4
tt.square()
perimeter = t5
perimeter.print_perimeter()
perimeter = t6
perimeter.print_perimeter()

m = []
h = []
n = random.randint(1,6)
for i in range(n):
    m.append(tt)
    h.append(perimeter)
print(sum(m),sum(h))

