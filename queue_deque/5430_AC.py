import re
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for _ in range(t) :
    p_lst = input() # 수행할 함수
    n = int(input()) # 배열에 들어있는 수의 개수
    if n == 0 :
        _ = input()
        queue = deque()
    else :
        queue = deque(i for i in re.split(r'\[|\]|,', input())[1:-1])
    flag = True
    turn = False
    for p in p_lst :
        if p == "R" :
            if turn :
                turn = False
            else :
                turn = True
        elif p == "D" :
            if len(queue) == 0 :
                flag = False
                break
            elif turn :
                queue.pop()
            else :
                queue.popleft()
        print(queue)
    if flag and len(queue) == 0 :
        answer = "[]"
    elif flag :
        answer = "["
        if turn :
            while queue :
                answer += f"{queue.pop()}," 
        else :
            while queue :
                answer += f"{queue.popleft()}," 
        answer = answer[:-1] + "]"
    else :
        answer = "error"
    print(answer)
        