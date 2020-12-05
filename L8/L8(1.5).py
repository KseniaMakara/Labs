import math
def function(a,b):
        f_1 = 15
        f_2 = 0
        d = math.tan(a)
        for i in range(1,6):
            f_1+=d
            d*= math.tan(a)
        for i in range(1,18,2):
            f_2+=math.sin(b)**i
        return (f_1,f_2)
print(function(2,6))
a=float(input('Enter a = '))
b=float(input('Enter b = '))
u=max(function(2,6))
print('u = {0}'.format(u))





