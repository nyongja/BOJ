from collections import deque

n, k = map(int, input().split()) # 벨트 길이, 종료 기준
a = list(map(int, input().split())) # 내구도 정보

robot_arr = [False for _ in range(2*n)]

tmp_a = []
for idx, v in enumerate(a) :
    tmp_a.append([v, idx])
a = tmp_a

for i in a : # 내구도가 0인 벨트 체크
    if a == 0 :
        k -= 1
step = 0
q = deque([]) # 현재 벨트 위에 있는 로봇 정보

def belt_loop() :
    global a, q, robot_arr
    # 벨트 회전
    a = [a[i-1] for i in range(len(a))]
    # 로봇 함께 회전
    new_q = deque([])
    while q :
        x = q.popleft()
        robot_arr[x] = False
        x += 1
        if x == n-1 : # 내리는 위치에 도달했으면 내리기
            continue
        robot_arr[x] = True
        new_q.append(x)
    q = new_q

    return

def robot_move() : # 로봇 직접 이동
    global a, q, k, robot_arr
    new_q = deque([])
    while q :
        x = q.popleft()
        if a[x+1][0] > 0 and robot_arr[x+1] == False: # 앞 칸이 내구성이 남아있고, 로봇도 없으면
            robot_arr[x] = False
            a[x+1][0] -= 1 
            if a[x+1][0] == 0 :
                k -= 1
            if x+1 == n-1 :
                continue
            x += 1
            robot_arr[x] = True
            new_q.append(x)
        else :
            new_q.append(x)
    q = new_q
    return

def on_robot() : # 로봇 태우기
    global a, q, k, robot_arr
    if a[0][0] > 0 :
        a[0][0] -= 1
        q.append(0)
        robot_arr[0] = True
        if a[0][0] == 0 :
            k -= 1
    return
        
while k > 0 :
    belt_loop()
    robot_move()
    on_robot()
    step += 1
print(step)