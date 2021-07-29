n = int(input())
array = [input() for _ in range(n)]
answer = ""

def quad_tree(x, y, n) :
    global array, answer
    check = array[x][y]
    
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if array[i][j] != check :
                answer += "("
                quad_tree(x, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                answer += ")"
                return
    if check == "0" :
        answer += "0"
    else :
        answer += "1"
    return

quad_tree(0, 0, n)
print(answer)