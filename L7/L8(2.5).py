def paralel(a, b):
    if (a[0]/b[0] == a[1]/b[1]) and (a[0]/b[0] != a[2]/b[2]):
        return True
    else:
        return False
n = int(input("Кількість прямих: "))
count = 0
lines = [[int(input('El [{0}][{1}]: '.format(i, j))) for i in range(3)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if paralel(lines[i], lines[j]):
            count += 1
for k in lines:
    print(k)
print(count/2)