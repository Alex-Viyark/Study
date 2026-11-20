'''
На странице каждой задачи онлайн-курсов "Поколения Python" имеется виджет, который отображает общее число учащихся, верно решивших задачу, и процент верных решений от общего числа попыток. Напишите программу, которая повторяет этот функционал: считает, сколько учеников верно решили задачу, и вычисляет процент верных решений среди всех попыток.
'''
#code
from decimal import*
n=int(input())
mat=[input().split(': ') for i in range(n)]
kol_corr=len([''.join(i) for i in mat if i[1]=='Correct'])
unic=len(set([''.join(i) for i in mat if i[1]=='Correct']))
if n!=0: v2=Decimal(f'{kol_corr/n*100}').quantize(Decimal('0'),rounding=ROUND_HALF_UP)
if kol_corr==0:print('Вы можете стать первым, кто решит эту задачу')
else: print(f'Верно решили {unic} учащихся',f'Из всех попыток {v2}% верных',sep='\n')
