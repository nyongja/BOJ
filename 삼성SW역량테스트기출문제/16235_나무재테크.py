from collections import deque
n, m, k = map(int, input().split()) # 땅 크기, 초기 나무 개수, 몇 년후
array = [list(map(int, input().split())) for _ in range(n)] # 매년 추가되는 양분 정보
ground = [[5 for _ in range(n)] for _ in range(n)] # 현재 땅에 있는 양분 정보
trees = [[deque([]) for _ in range(n)] for _ in range(n)] # [] 현재 땅에 있는 나무 정보

for _ in range(m) :
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def chk_pos(a, b) :
    if a < 0 or a >= n or b < 0 or b >= n :
        return False
    return True

def spring() :
    new_trees = []
    for i in range(n) :
        for j in range(n) :
            num = len(trees[i][j])
            for k in range(num) :
                if ground[i][j] >= trees[i][j][k] :
                    ground[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                    if trees[i][j][k] % 5 == 0 :
                        new_trees.append((i, j))
                else : # 여름
                    for _ in range(k, num) :
                        ground[i][j] += trees[i][j].pop() // 2
                    break
            ground[i][j] += array[i][j]
    for i, j in new_trees :
        for k in range(8) :
            ni, nj = i + dx[k], j + dy[k]
            if chk_pos(ni, nj) :
                trees[ni][nj].appendleft(1)
for _ in range(k) : # k년 동안
    spring()

answer = 0
for i in range(n) :
    for j in range(n) :
        answer += len(trees[i][j])
print(answer)