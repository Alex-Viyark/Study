'''
Напишите программу для вычисления суммы двух матриц.
'''
#code
n,m=map(int,input().split())
mat1=[[int(i) for i in input().split()] for j in range(n)]
input()
mat2=[[int(i) for i in input().split()] for j in range(n)]
mat=[[mat1[i][j]+mat2[i][j] for j in range(m)] for i in range(n)]
[print(*row) for row in mat]



