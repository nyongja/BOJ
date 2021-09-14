import sys
input = sys.stdin.readline

N = int(input())
matrix = [(0, 0)]
s = [0 for _ in range(N+1)]

for i in range(1, N+1) :
    r, c = map(int, input().split())
    matrix.append((r, c))
    s[i] = s[i-1] + r*c # 누적 합 구하기

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(2, N+1) : # 행렬 곱의 길이
    for j in range(1, N-i+2) : # 시작점 
        dp[j][j+i-1] = min([dp[j][j+k] + matrix[j][0] * matrix[j+1+k][0] * matrix[j+i-1][1] + dp[j+1+k][j+i-1] for k in range(i-1)])
#print(dp)
print(dp[j][-1])