n = int(input())
answer = 0
# 5가 등장하는 만큼 0이 늘어남
for i in range(1, n + 1) :
    while i % 5 == 0 :
        answer += 1
        i /= 5
print(answer)