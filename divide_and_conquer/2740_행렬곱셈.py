n, m = map(int, input().split()) # 행렬 A의 크기 
A = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split()) # 행렬 B의 크기
B = [list(map(int, input().split())) for _ in range(m)]

answer = []

for a in range(n) :
    answer.append([])
    for b in range(k) :
        tmp = 0
        for i in range(m) :
            tmp += A[a][i] * B[i][b]
        answer[a].append(tmp)

for ans in answer :
    print(*ans)