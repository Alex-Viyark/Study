def check_winners(scores,student_score):
    print(['Вы не попали в тройку победителей.','Вы в тройке победителей!'][student_score in sorted(scores,reverse=True)[:3]])
'''
тест
scores_1=[3,2335,54,14,4,642,9,25,0,32,5]
Stas=3
check_winners(scores_1,Stas)

scores_1=[3,2335,54,14,4,642,9,25,0,32,5]
Stas=642
check_winners(scores_1,Stas)
'''
