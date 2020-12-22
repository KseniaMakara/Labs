class TFraction():
    def __init__(self, numerator=0, denominator=0):
        self.numerator = numerator
        self.denominator = denominator

    def print_numerator(self):
        self.numerator = int(input('enter numerator = '))
        print('Numerator is = {0} '.format(self.numerator))

    def print_denominator(self):
        self.denominator = int(input('enter denominator = '))
        print("Denominator is = {0}".format(self.denominator))

    def incresing_number(self):
        increase = float(input('enter digit for increasing = '))
        print(self.numerator/self.denominator + increase)

    def reducing_number(self):
        reduce = float(input('enter digit for reducing = '))
        print(self.numerator/self.denominator - reduce)

# __________
# n = TFraction()
# n.print_numerator()
# n.print_denominator()
# n.incresing_number()
# n.reducing_number()


