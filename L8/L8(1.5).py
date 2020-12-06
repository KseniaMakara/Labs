import math
def function(c,d):
    d = math.tan(a)
    if a<=3:
        f_1 = 15
        for i in range(1,6):
            f_1+= d
            d*= math.tan(a)
    else:
        f_1 = 0
        for i1 in range(1, 18, 2):
            f_1 += math.sin(a) ** i1
    if b > 3:
        f_2 = 0
        for i1 in range(1,18,2):
            f_2+=math.sin(b)**i1
    else:
        f_2 = 15
        for i in range(1,6):
            f_2+= d
            d*= math.tan(a)
    return (f_1,f_2)
a = float(input('Enter a = '))
b = float(input('Enter b = '))
print(function(a,b))
u=max(function(a,b))
print('u = {0}'.format(u))











