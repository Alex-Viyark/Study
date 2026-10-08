"""
Напишите программу, которая меняет местами столбцы в матрице.
"""
#код
n,m=int(input()),int(input())
mat=[input().split() for i in range(n)]
i=input().split()
i,j=int(i[0]),int(i[1])
for row in mat:
    row[i],row[j]=row[j],row[i]
[print(*row) for row in mat]
