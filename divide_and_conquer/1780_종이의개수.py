n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
count_m1 = 0
count_0 = 0
count_1 = 0

def cut(x, y, n) :
    global count_m1, count_0, count_1
    check = array[x][y]
    for i in range(x, x + n) :
        for j in range(y, y + n) :
            if check != array[i][j] :
                n_3 = n//3
                cut(x, y, n_3)
                cut(x+n_3, y, n_3)
                cut(x+n_3*2, y, n_3)
                cut(x, y+n_3, n_3)
                cut(x+n_3, y+n_3, n_3)
                cut(x+n_3*2, y+n_3, n_3)
                cut(x, y+n_3*2, n_3)
                cut(x+n_3, y+n_3*2, n_3)
                cut(x+n_3*2, y+n_3*2, n_3)
                return
    if check == -1 :
        count_m1 += 1
    elif check == 0 :
        count_0 += 1
    else :
        count_1 += 1
    return

cut(0, 0, n)
print(count_m1)
print(count_0)
print(count_1)
