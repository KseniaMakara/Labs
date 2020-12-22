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
    def sides(self):
        a1 = ((self.x1-self.x2)**2 + (self.y1 - self.y2)**2)**1/2
        a2 = ((self.x2-self.x3)**2 + (self.y2 - self.y2)**3)**1/2
        b1 = ((self.x3-self.x4)**2 + (self.y3 - self.y4)**2)**1/2
        b2 = ((self.x4-self.x1)**2 + (self.y4 - self.y1)**2)**1/2
        @property
        def compare_sides(self):
            if a1 == a2 and b1 == b2:
                a = a1
                b = b1
                print('It is a rectangle')
            elif a1 == b1 and b2 == a2:
                a = a1
                b = b2
                print('It is a rectangle')
            elif a1 == b2 and a2 == b1:
                a = a1
                b = b1
                print('It is a rectangle')
            else:
                raise Exception('Another figure')

            def __getitem__(self, key, value):
                if key == 1:
                    return self.a
                elif key == 2:
                    return self.b
                else:
                    raise Exception('Wrong key')
            def squre(self):
                s = a*b
                print(s)
            def perimeter(self):
                p = 2*(a+b)
                print(p)

