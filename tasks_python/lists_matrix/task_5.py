"""
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.
"""
#код
n=int(input())
mat=[[int(ch) for ch in input().split()] for i in range(n)]
up=sum([mat[i][j] for i in range(n) for j in range(n) if i<j and i+j+1<n])
down=sum([mat[i][j] for i in range(n) for j in range(n) if i>j and i+j+1>n])
right=sum([mat[i][j] for i in range(n) for j in range(n) if i<j and i+j+1>n])
left=sum([mat[i][j] for i in range(n) for j in range(n) if i>j and i+j+1<n])
print(f'''
Верхняя четверть: {up}
Правая четверть: {right}
Нижняя четверть: {down}
Левая четверть: {left}
''')
