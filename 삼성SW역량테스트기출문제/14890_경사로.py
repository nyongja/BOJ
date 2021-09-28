import sys
input = sys.stdin.readline

n, l = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 가로로 살펴보기
for i in range(n) :
    height = array[i][0]
    cnt = 0
    visited = [False] * n
    flag = True
    for j in range(n) :
        if flag :
            if array[i][j] == height :
                continue
            elif array[i][j] == height + 1 : # case1. 한 칸 위
                if j-l >= 0 :
                    for k in range(1, l+1) :
                        if not visited[j-k] and array[i][j-k] == height :
                            visited[j-k] = True
                        else :
                            flag = False
                else :
                    flag = False
            elif array[i][j] == height - 1 : # case 2. 한 칸 밑
                if j+l-1 < n :
                    for k in range(l) :
                        if not visited[j+k] and array[i][j+k] == height - 1 :
                            visited[j+k] = True
                        else :
                            flag = False
                else :
                    flag = False
            else : flag = False
            height = array[i][j]
    if flag :
        ans += 1
# 세로로 살펴보기
for i in range(n) :
    height = array[0][i]
    cnt = 0
    visited = [False] * n
    flag = True
    for j in range(n) :
        if flag :
            if array[j][i] == height :
                continue
            elif array[j][i] == height + 1 : # case1. 한 칸 위
                if j-l >= 0 :
                    for k in range(1, l+1) :
                        if not visited[j-k] and array[j-k][i] == height :
                            visited[j-k] = True
                        else :
                            flag = False
                else :
                    flag = False
            elif array[j][i] == height - 1 : # case 2. 한 칸 밑
                if j+l-1 < n :
                    for k in range(l) :
                        if not visited[j+k] and array[j+k][i] == height - 1 :
                            visited[j+k] = True
                        else :
                            flag = False
                else :
                    flag = False
            else : 
                flag = False
            height = array[j][i]
    if flag :
        ans += 1

print(ans)