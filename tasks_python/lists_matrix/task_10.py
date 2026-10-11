#код
n = int(input())

def matr_sum(mat, _):
    return sum(sum(row) for row in mat)

mat = [[int(i) for i in input().split()] for j in range(n)]

sp = [i for i in range(1, n**2 + 1)]

if all(sp[i] in mat for i in range(n)):
    s = sum(mat[0])
    if all(sum(mat[i]) == s for i in range(n)):
        if sum([mat[i][j] for i in range(n) for j in range(n) if i == j]) == s:
            if sum([mat[n - j - 1][n - i - 1] for i in range(n) for j in range(n) if i == j]) == s:
                mt = [[mat[j][i] for i in range(n)] for j in range(n)]
                if all(sum(mat[x]) == s for x in range(n)):
                    print('YES')
                else:
                    print('NO')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
