import random
class Rectangle():
    def __init__(self, x1=0, x2=0, x3 = 0, x4 = 0, y1 = 0, y2 = 0, y3 = 0, y4 = 0):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4
    def print_x_y(self):
        self.x1 = random.randint(-5,5)
        self.x2 = random.randint(-5,5)
        self.x3 = random.randint(-5,5)
        self.x4 = random.randint(-5,5)
        self.y1 = random.randint(-5,5)
        self.y2 = random.randint(-5,5)
        self.y3 = random.randint(-5,5)
        self.y4 = random.randint(-5,5)

    def calc_a(self):
        return ((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)**1/2

    def calc_b(self):
        return ((self.x3 - self.x4)**2 + (self.y3 - self.y4)**2)**1/2

    def __getitem__(self, key, value):
        if key == 1:
            return self.a
        elif key == 2:
            return self.b
        else:
            raise Exception('Wrong key')
    def squre(self):
        return self.calc_a()*self.calc_b()

    def perimeter(self):
        return  2*(self.calc_a()+self.calc_b())
