class TNumber():
    def init(self, n=0, m=0):
        self.numbers = n
        self.m = list(map(int, list(str(n))))
    def enter_n(self):
        self.numbers = input('Enter n = ')
        self.m = list(map(int, list(str(self.numbers))))
        return self.numbers

    def printn(self):
        print(self.numbers)

    def count(self):
        k = int(input('k = '))
        return self.m.count(k)

    def sum(self):
        return sum(self.m)

    def gt(self, other):
        return self.numbers < other.numbers
