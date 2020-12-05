# і рядки, j стовпці
n=int(input("Enter n = "))
matrix = []
el=0
k=1
b1=1
b=[]
for i in range(n):
    r = []
    for j in range(n):
        if (i+j) % 2 == 0:
            for k in range(1,i+1):
                el +=k
        if (i+j)%2!=0:
            for k in range(1,j + 1):
                el +=k**2
        r.append(el)
    matrix.append(r)
print('r = {0}'.format(r))
print('matrix = {0}'.format(matrix))
for j in range(n):
    dob = 1
    for i in range(n):
        dob *= matrix[i][j]
    b.append(dob)
print('b ={0} '.format(b))
m=[]
for i in range(len(b)):
    if b[i]%2==0:
        m.append(b[i])
print(max(m))
