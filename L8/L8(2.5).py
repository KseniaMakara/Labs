def func(i):
    for i in range(n):
        k=[]
        for j in range(n):
            if (a[i]/b[j])==(a[i]/b[j]):
                for i1 in range(j):
                    k.append(i1)
                return k
n = int(input('n = '))
a = [float(input('Коефіцієнт a[{0}]='.format(i))) for i in range(n)]
print(a)
b = [float(input('Коефіцієнт b[{0}]='.format(i))) for i in range(n)]
print(b)
print(func(n))
