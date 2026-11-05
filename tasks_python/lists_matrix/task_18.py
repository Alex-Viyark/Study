'''
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n, заполнив ее в соответствии с образцом.
'''
#code
n=int(input())
[print(*['1'.ljust(3) if (i>=j and i>=n-1-j) or (i<=j and i<=n-1-j) else '0'.ljust(3) for j in range(n)]) for i in range(n)]
