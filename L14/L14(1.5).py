import random
class TTriangle():

    def print_perimeter(self):
        return self.a+self.b + self.c

    def square(self):
        p = self.a + self.b + self.c
        h_p = p/2
        return (h_p(h_p-self.a)(h_p-self.b)(h_p-self.c))**1/2

class ETriangle(TTriangle): # рівносторонній
    def __init__(self, a=0):
        self.a = a
    def print_a_b_c(self):
        self.a = float(input(' Enter first side = '))
        print(a)

    def print_perimeter(self):
        return 3*self.a

    def square(self):
        p = 2*self.a + self.b
        h_p = p/2
        return (3**1/2)*self.a**2/4

class ITriangle(TTriangle): #рівнобедрений
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def print_a_b_c(self):
        self.a = float(input(' Enter first side = '))
        self.b = float(input(' Enter second side = '))

    def print_perimeter(self):
        return 2*self.a+self.b

    def square(self):
        p = 2*self.a + self.b
        h_p = p/2
        return (h_p*(h_p-self.a)*(h_p-self.b)*(h_p-self.a))**1/2

class RTriangle(TTriangle): #прямокутний
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def print_a_b_c(self):
        self.a = float(input(' Enter first side = '))
        self.b = float(input(' Enter second side = '))

    def print_perimeter(self):
        return self.a+self.b+((self.a)**2+(self.b)**2)**1/2

    def square(self):
        return self.a*self.b/2

classes = [ETriangle, ITriangle, RTriangle]
objects = [classes[random.randint(0,2)](random.randint(3,25),random.randint(3,25)) for el in range(100)]
sum_eq = 0
sum_other = 0
for obj in objects:
    if obj.__class__ == ITriangle:
        sum_eq+=obj.print_perimeter()
    else:
        sum_other+=obj.square()
print(sum_eq,sum_other)


