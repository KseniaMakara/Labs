class Triangle():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
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

    def __lt__(self, other_triangle):
        if t1 < t2:
            print("tr is considered as lower than tr2")
            return self.get_s() < other_triangle.s()
##
t1=Triangle()
t1.print_a()
t1.print_b()
s = t1.get_s()
t2=Triangle()
t2.print_a()
t2.print_b()
t2.get_s()