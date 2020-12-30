class Triangle():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def print_a(self):
        self.a = float(input('enter a = '))
        print('First leg = {0}'.format(self.a))
    def print_b(self):
        self.b = float(input('enter b = '))
        print('First leg = {0}'.format(self.b))
    def get_s(self):
        return  self.a*self.b/2

    def get_perimeter(self):
        c = (self.a**2+self.b**2)**1/2
        return self.b+self.b+c

    def __lt__(self, other):
        return self.get_s() < other.get_s()

    def __add__(self, other):
        return Triangle(other.a + self.a, other.b + self.b)

    def __sub__(self, other):
        return Triangle( self.a - other.a, self.b -other.b )

    def __mul__(self, other):
        return (other * self.a, other * self.b)
##
t1=Triangle()
t1.print_a()
t1.print_b()
s = t1.get_s()
t2=Triangle()
t2.print_a()
t2.print_b()
t2.get_s()



