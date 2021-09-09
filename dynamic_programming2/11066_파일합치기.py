import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    K = int(input())
    file = list(map(int, input().split()))
    dp = [[0 for _ in range(K+1)] for _ in range(K+1)]
    s = [0 for _ in range(K+1)]

    for i in range(1, K+1) :
        s[i] = s[i-1] + file[i-1]
    
    for i in range(2, K+1) : # 부분 파일의 길이
        for j in range(1, K-i+2) : # 시작점
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (s[j+i-1] - s[j-1])
    print(dp[1][K])