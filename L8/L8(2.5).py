import random
n=int(input('Enter n = '))
m=int(input('Enter m = '))
a = [[random.randint(-100,100) for i in range(n)] for j in range(m)]
def print_matrix(a):
    for el in a:
        print(el)
print_matrix(a)
k = 0
for j in range(m):
    for i in range(n):
        if a[i][j]>0:
            k+=1
print(k)
