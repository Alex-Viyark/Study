'''
Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.
'''
#код
n=int(input())
mat=[input().split() for i in range(n)]
mt=[[mat[i][j] for i in range(n-1,-1,-1)] for j in range(n)]
[print(*row) for row in mt]


