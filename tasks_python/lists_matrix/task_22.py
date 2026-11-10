'''
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m, заполнив ее "диагоналями" в соответствии с образцом.
'''
#code
n, m = [int(el) for el in input().split()]
matrix = [[None for _ in range(m)] for _ in range(n)]
cnt = 1

# проходим по всем диагоналям
for d in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == d:
                matrix[i][j] = cnt
                cnt += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()
