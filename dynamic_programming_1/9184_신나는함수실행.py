array = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def dp(a, b, c) :
    global array
    if a <= 0 or b <= 0 or c <= 0 :
        return array[0][0][0]
    elif a > 20 or b > 20 or c > 20 :
        return dp(20, 20, 20)
    elif array[a][b][c] == 0 : # 결과가 아직 계산되지 않은 경우
        if a < b and b < c :
            array[a][b][c] = dp(a, b, c-1) + dp(a, b-1, c-1) - dp(a, b-1, c)
        else :
            array[a][b][c] = dp(a-1, b, c) + dp(a-1, b-1, c) + dp(a-1, b, c-1) - dp(a-1, b-1, c-1)
    return array[a][b][c]

array[0][0][0] = 1

while True :
    a, b, c = map(int, input().split())
    if a == b == c == -1 :
        break
    print(f"w({a}, {b}, {c}) =", dp(a, b, c))
