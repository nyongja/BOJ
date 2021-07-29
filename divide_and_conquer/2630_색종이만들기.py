from re import S

n = int(input())
array = [list((map(int, input().split()))) for _ in range(n)]

white = 0
blue = 0

def check_color(x, y, n) :
    global white, blue, array
    color = array[x][y]

    for i in range(x, x + n) :
        for j in range(y, y + n) :
            if color != array[i][j] :
                check_color(x, y, n//2) # 1사분면
                check_color(x, y+n//2, n//2) # 2사분면
                check_color(x+n//2, y, n//2) # 3사분면
                check_color(x+n//2, y+n//2, n//2) # 4사분면
                return

    if color == 0 :
        white += 1
    elif color == 1 :
        blue += 1
    return

check_color(0, 0, n)
print(white)
print(blue)
