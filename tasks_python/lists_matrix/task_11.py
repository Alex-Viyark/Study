'''
Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.
'''
#код
n=int(input())
mat=[input().split() for i in range(n)]
rmat=[[mat[i][j] for j in range(n)] for i in range(n-1,-1,-1)]
[print(*row) for row in rmat]

