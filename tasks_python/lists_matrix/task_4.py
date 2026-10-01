"""
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.
"""
#код
n=int(input())
mat=[input().split() for i in range(n)]
k=0
for st in mat:
    sr=sum(map(int,st))/len(st)
    for i in st:
        if int(i)>sr:
            k+=1
    print(k)
    k=0
