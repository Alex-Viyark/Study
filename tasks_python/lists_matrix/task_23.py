'''
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m, заполнив ее "спиралью" в соответствии с образцом.
'''
#code
n,m=map(int,input().split())
mat=[[0 for j in range(m)] for i in range(n)]
row=0
col=0
r,d,l,u=1,0,0,0
counter=1
for hod in range(2*n-1):
    if counter == n * m + 1: break
    if r==1:
        for j in range(col,m-row):
                mat[row][j]=str(counter).ljust(3)
                counter+=1
        col=m-row-1
        row+=1
        r,d=0,1
    elif d==1:
        for i in range(row,n+1-row):
                mat[i][col]=str(counter).ljust(3)
                counter+=1
        row=n-row
        col-=1
        d,l=0,1
    elif l==1:
        for j in range(col,n-row-2,-1):
                mat[row][j]=str(counter).ljust(3)
                counter+=1
        col=n-row-1
        row-=1
        l,u=0,1
    elif u==1:
        for i in range(row,col,-1):
                mat[i][col]=str(counter).ljust(3)
                counter+=1
        row=col+1
        col+=1
        u,r=0,1
[print(*row) for row in mat]
