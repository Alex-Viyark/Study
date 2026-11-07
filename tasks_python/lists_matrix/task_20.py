'''
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m, заполнив ее "змейкой" в соответствии с образцом.
#code
n,m=map(int,input().split())
mat=[[str(m*i+j).ljust(3) for j in range(1,m+1)] if i%2==0 else [str(m*i+j).ljust(3) for j in range(1,m+1)][::-1] for i in range(n)]
[print(*row) for row in mat]



