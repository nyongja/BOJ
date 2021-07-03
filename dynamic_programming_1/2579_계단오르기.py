n = int(input())
array = [int(input()) for _ in range(n)]
answer = [0 for _ in range(n)]

for i in range(n) :
    if i == 0 :
        answer[i] = array[i]
    elif i == 1 :
        answer[i] = array[i-1] + array[i]
    elif i == 2 :
        answer[i] = max(answer[i-2] + array[i] , array[i-1] + array[i])
    # 계단 3층 부터 조건
    # 이전 칸 선택 안할 시 3계단 중복 될 이유 없으니까 + 그냥 내 계단 or 이전 칸 선택 시 이전 이전 칸은 선택하면 안되므로 3칸 전 + 이전 칸 선택 + 내계단
    else :
        answer[i] = max(answer[i-2] + array[i], answer[i-3] + array[i-1] + array[i])

print(answer[n-1])
