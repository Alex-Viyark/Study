'''
Даны оценки по информатике трех учеников по 10-балльной шкале. Напишите программу, выводящую множество оценок, которые есть и у первого, и у второго учеников, но которых нет у третьего ученика.
'''
#code
print(*sorted(set(int(i) for i in input().split())&set(int(i) for i in input().split())-set(int(i) for i in input().split()),reverse=True))
