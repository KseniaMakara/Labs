class Number:
    def __init__(self,_n, _amount_of_figures, _mass, _figure_in_mass, _count, _el, _sum):
        self.n = _n
        self.amount_of_figures = _amount_of_figures
        self.mass = _mass
        self.figure_in_mass = _figure_in_mass
        self.el = _el
        self.count = _count
        self.sum = _sum
    def print_n(self):
        self.n = int(input('Enter n = '))
        print('n = {0}'.format(self.n ))
    def print_count(self):
        self.el = int(input('enter el for mass:'))
    def amount_of_figures(self):
        self.amount_of_figures = 0
        self.mass = []
        while self.n>0:
            self.n//=10
            self.mass.append(self.n%10)
            self.amount_of_figures+=1
        print(self.amount_of_figures,)
    def count_figure(self):
        self.count = self.mass.count(self.el)
        print(self.count)
    def sum(self):
        self.sum = 0
        for elem in self.mass:
            self.sum+=elem
        print(self.sum)





