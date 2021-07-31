def matrix_mul(n, m1, m2) :
    result = []
    for i in range(n) :
        result.append([])
        for j in range(n) :
            tmp = 0
            for k in range(n) :
                tmp += m1[i][k] * m2[k][j]
            tmp %= 1000
            result[i].append(tmp)
    return result

def divide(n, b, m) :
    if b == 1 :
        return m
    elif b == 2 :
        return matrix_mul(n, m, m)
    else :
        tmp = divide(n, b//2, m)
        if b%2 :
            return matrix_mul(n, matrix_mul(n, tmp, tmp), m)
        else : 
            return matrix_mul(n, tmp, tmp)

n, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

answer = divide(n, b, A)
for ans in answer :
    for i in ans :
        print(i%1000, end = ' ')
    print('')