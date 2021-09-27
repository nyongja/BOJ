import sys
import math
input = sys.stdin.readline

n = int(input()) # 시험장 개수
num = list(map(int, input().split())) # 각 시험장에 있는 응시자 수
b, c = map(int, input().split())

ans = 0
for i in range(len(num)) :
    num[i] -= b
    if num[i] > 0 :
        ans += (1 + (math.ceil(num[i]/c)))
    else :
        ans += 1
print(ans)