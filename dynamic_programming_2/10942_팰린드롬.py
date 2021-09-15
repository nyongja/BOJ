import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
M = int(input()) # 질문 개수
dp = [[0 for _ in range(N)] for _ in range(N)]

for num_len in range(N+1) : # 펠림드롬 길이
    for start in range(N - num_len) : 
        end = start + num_len
        
        if start == end : # 펠린드롬 길이가 하나면
            dp[start][end] = 1
        elif num[start] == num[end] : # 끝자리가 서로 같으면
            if start + 1 == end : # 길이가 2짜리 
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1 :
                dp[start][end] = 1
                
for _ in range(M) :
    s, e = map(int, input().split())
    print(dp[s-1][e-1])