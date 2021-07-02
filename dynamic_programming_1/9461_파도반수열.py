t = int(input())
array = [0] * 101

for idx, num in enumerate([0, 1, 1, 1, 2, 2]) : # 초기값 계산
    array[idx] = num

def dp(n) :
    global array
    if array[n] != 0 :
        return array[n]
    array[n] = dp(n-1) + dp(n-5) # 바로 전 삼각형 + 5 전 삼각형의 길이 => 현재 삼각형 변의 길이
    return array[n]

for _ in range(t) :
    n = int(input())
    print(dp(n))