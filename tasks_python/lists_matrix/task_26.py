'''
возведение матрицы в степень
'''
# code
n=int(input())
mat=[[int(i) for i in input().split()] for j in range(n)]
m=int(input())
matr=mat
for z in range(m-1):
    matr=[[(sum([matr[i][r]*mat[r][j] for r in range(n)])) for j in range(n)] for i in range(n)]
[print(*row) for row in matr]









