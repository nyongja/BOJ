from collections import deque
from tabnanny import check

def solution(M, N, array) :
    visited = [[-1] * M for _ in range(N)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    def check_pos(x, y) :
        if 0 <= x < N and 0 <= y < M :
            return True
        return False

    q = deque([(0, 0)])
    visited[0][0] = 0
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if check_pos(nx, ny) :# 이동 가능한 경우
                # 이미 방문했으면
                if visited[nx][ny] != -1 :
                    if array[nx][ny] == 1 : # 벽이 있는 곳이면
                        # 기존에 알고 있던 벽 부순 개수 > 지금 방문했을 때 벽 부순 개수 + 1
                        if visited[nx][ny] > visited[x][y] + 1 :
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx, ny))
                    elif array[nx][ny] == 0 :  # 벽이 없는 곳이면
                        if visited[nx][ny] > visited[x][y] :
                            visited[nx][ny] = visited[x][y]
                            q.append((nx, ny))
                # 아직 방문하기 이전이면
                elif visited[nx][ny] == -1 :
                    if array[nx][ny] == 1 : # 벽이 있는 곳이면
                        visited[nx][ny] = visited[x][y] + 1
                    elif array[nx][ny] == 0 : # 벽이 없는 곳이
                        visited[nx][ny] = visited[x][y]
                    q.append((nx, ny))

    return visited[-1][-1]


M, N = map(int, input().split()) # 가로, 세로
array = list(list(map(int, input().strip())) for _ in range(N))
print(solution(M, N, array))