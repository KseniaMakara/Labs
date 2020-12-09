import random
n=int(input('Enter n = '))
m=int(input('Enter m = '))
a = [[float(input("a[{0}][{1}]=".format(i, j))) for j in range(n)] for i in range(n)]
k=0
def print_matrix(a):
    for el in a:
        print(el)
print_matrix(a)
def is_paralel(l1,l2):
    return l1[0]/l2[0]==l1[1]/l2[1]

for i in range(n-1):
    for j in range(i+1,n):
        if (is_paralel(a[i],a[j])):
            k+=1
print(k)
