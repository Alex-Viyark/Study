"""
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
"""
#код
n=int(input())
mat=[input().split() for i in range(n)]
if all(mat[i][j]==mat[j][i] for i in range(n) for j in range(n)): print('YES')
else: print('NO')
