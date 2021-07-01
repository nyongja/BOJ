t = int(input())

def fibonacci(n) :
    global array
    zero, one = array[n-1]
    zero2, one2 = array[n-2]
    return zero + zero2, one + one2


max_n = 1 # 현재 몇번째 피보나치까지 구했는지
array = [(1, 0), (0, 1)] # 각각 zero, one이 필요한 양

for _ in range(t) :
    num = int(input())
    
    if num > max_n : # 이미 구한 피보나치는 그냥 값 가져오면 되므로
        for i in range(max_n + 1, num + 1) :
            array.append((fibonacci(i)))
        max_n = num

    print(*array[num])
