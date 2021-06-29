board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
flag = False

def is_promising(i, j) :
    promising = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for k in range(9) :
        # 행 체크
        if board[i][k] in promising :
            promising.remove(board[i][k])
        # 열 체크
        if board[k][j] in promising :
            promising.remove(board[k][j])
    
    # 사각형 체크
    # 몫을 통해서 몇 번째 스도쿠 칸인지 체크 
    i //= 3 
    j //= 3 
    for p in range(i*3, (i+1) * 3) :
        for q in range(j*3, (j+1) * 3) :
            if board[p][q] in promising :
                promising.remove(board[p][q])
    return promising

def sudoku(x) :
    global flag
    
    if flag : # 이미 답이 출력된 경우
        return
    
    if x == len(zeros) : # 마지막 0까지 다 채웠을 경우
        for row in board :
            print(*row)
        flag = True
        return
    
    else :
        (i, j) = zeros[x]
        promising = is_promising(i, j) # 가능한 숫자들

        for num in promising : # 가능한 숫자 하나씩 넣어보기
            board[i][j] = num
            sudoku(x+1) # 다음 zero 칸
            board[i][j] = 0 # 정답이 없을 경우를 대비해서 초기화

sudoku(0)