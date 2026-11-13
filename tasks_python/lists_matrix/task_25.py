'''
Напишите программу, которая перемножает две матрицы.
'''
#code
n,m=map(int,input().split())
mat1=[[int(i) for i in input().split()] for j in range(n)]
input()
m,k=map(int,input().split())
mat2=[[int(i) for i in input().split()] for j in range(m)]
mat=[[str(sum([mat1[i][r]*mat2[r][j] for r in range(m)])).ljust(3) for j in range(k)] for i in range(n)]
[print(*row) for row in mat]




