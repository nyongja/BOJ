n = int(input())
array = list(map(int, input().split()))
op_num = list(map(int, input().split())) # + , -, *, /

max_result = -1 * int(1e9)
min_result = int(1e9)

def dfs(x) :
    global max_result
    global min_result

    if x == len(array) - 1 : # 전체 다 계산 한 경우
        if max_result < array[-1] :
            max_result = array[-1]
        if min_result > array[-1] :
            min_result = array[-1]
        return

    else :
        for idx, op in enumerate(op_num) :
            if op_num[idx] != 0 :
                prev = array[x+1]
                if idx == 0 :
                    array[x+1] = array[x] + array[x+1]
                elif idx == 1 :
                    array[x+1] = array[x] - array[x+1]
                elif idx == 2 :
                    array[x+1] = array[x] * array[x+1]
                else :
                    prev = array[x+1]
                    if array[x] < 0 : # 음수인 경우 -> 양수로 바꾼 후 다시 음수 처리
                        array[x+1] = -(abs(array[x]) // array[x+1])
                    else :
                        array[x+1] =  array[x] // array[x+1]
                op_num[idx] -= 1
                dfs(x+1)
                array[x+1] = prev # 해당 케이스틑 다 봤으니 이전 값응로 되돌림(중복 계산 방지)
                op_num[idx] += 1
        
dfs(0)
print(max_result)
print(min_result)
             

