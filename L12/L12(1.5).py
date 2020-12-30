class Triangle():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    @property
    def a(self):
        return self.a
    @a.setter
    def a(self, value):
        if value>0:
            self.__a = value
        else:
            raise Exception('must be positive')
    @property
    def b(self):
        return self.b
    @b.setter
    def b(self, value):
        if value > 0:
            self.__b = value
        else:
            raise Exception('must be positive')
    def print_a(self):
        self.a = float(input('enter a = '))
        return self.a
    def print_b(self):
        self.b = float(input('enter b = '))
        return self.b
    def __getitem__(self, key, value):
        if key == 1:
            return self.a
        elif key == 2:
            return self.b
        else:
            raise Exception('Wrong key')
    def get_s(self):
        s = self.a*self.b/2
        print(s)
        return s
    def get_perimeter(self):
        c = (self.a**2+self.b**2)**1/2
        p = self.b+self.b+c
        print(p)
        return p

    def __lt__(self, othere):
        return s < other.s

    def __add__(self, other):
        return Triangle(other.a + self.print_a, other.b + self.print_b)

    def __sub__(self, other):
        return Triangle(other.a - self.print_a, other.b - self.print_b)

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
