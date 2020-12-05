def func(i):
    if i == 0 or i==1:
        return 1
    else:
        return func((i-1))+func(i-2)
n = int(input('n = '))
print('х_{0} = {1}'.format(n, func(n)))