n = int(input())
cnt = 0

board = [0] * n

def check(idx) :
    # 대각선에서 만나는 조건
    # 열의 차이 = 행의 차이
    for i in range(idx) :
        if (board[idx] == board[i]) or (idx - i == abs(board[idx] - board[i])) : # 같은 열에 있거나, 대각선에서 만난다면
            return False
    return True

def nqueen(idx) :
    global cnt
    if idx == n :
        cnt += 1
        return
    for i in range(n) :
        board[idx] = i
        if check(idx) :
            nqueen(idx + 1)

nqueen(0)
print(cnt)