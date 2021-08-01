n = int(input())
m = [[1, 1], [1, 0]]

def matrix_mul(m_len, m1, m2) :
    result = []
    for i in range(m_len) :
        result.append([])
        for j in range(m_len) :
            tmp = 0
            for k in range(m_len) :
                tmp += m1[i][k] * m2[k][j]
            result[i].append(tmp % 1000000007)
    return result

def divide(m_len, n, m) :
    if n == 1 :
        return m
    else :
        tmp = divide(m_len, n//2, m)
        if n % 2 : # 홀수
            return matrix_mul(m_len, matrix_mul(m_len, tmp, tmp), m)
        else : # 짝수
            return matrix_mul(m_len, tmp, tmp)

answer = divide(2, n, m)
print(answer[0][1] % 1000000007)