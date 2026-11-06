'''
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m, заполнив ее в соответствии с образцом.
'''
#code
n,m=map(int,input().split())
row1=[i for i in range(1,m+1)]
mat=[row1[i%m:m]+row1[0:i%m] for i in range(n)]
[print(*row) for row in mat]
