class Number():
    def __init__(self, n):
        self.numbers = n
    def enter_n(self):
        self.numbers = input('Enter n = ')
    def get_digits(self):
        print(len(self.numbers.split(',')))
    def get_number(self):
        print(self.numbers)
    def count_n(self):
        el = int(input("Element in massive = "))
        b = self.numbers.split(',')
        g = 0
        for i in range(len(self.numbers.split(','))):
            if el == int(b[i]):
                g+=1
        print(g)
    def get_sum(self):
        s=0
        for i in range(len(self.numbers.split(','))):
            a = self.numbers.split(',')
            s+=int(a[i])
        print(s)
    def __gt__(self, other):
        if len(s)!=len(p):
            if len(s)>len(p):
                return True
            else:
                return False
        return False

    # def get_len(self):
    #     return len(self.digits)
#_________________________________________________
p = Number('5,6,3,6,9,4')
s = Number('8,4,6,3')
p.get_number()
p.get_sum()
p.count_n()


