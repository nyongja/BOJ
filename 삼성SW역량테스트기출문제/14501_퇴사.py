import sys
input = sys.stdin.readline

n = int(input())
array = []
ans = [0] * (n+1)
for _ in range(n) :
    t, p = map(int, input().split())
    array.append((t, p))

for i in range(n-1, -1, -1) :
    t, p = array[i]
    if i+t > n : # 퇴사 전에 상담을 끝낼 수 없다면
        ans[i] = ans[i+1]
    else : # 끝낼 수 있는 상담이라
        ans[i] = max(ans[i+1], ans[i+t]+p)
print(ans[0])

