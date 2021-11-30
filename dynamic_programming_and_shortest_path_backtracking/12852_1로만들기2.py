n = int(input())
INF = int(1e9)
array = [INF] * (n+1)
how = [0] * (n+1)
array[1] = 0
how[1] = [1]

for i in range(2, n+1) :
    # 3 곱하기
    if i % 3 == 0 :
        prev = array[i]
        array[i] = min(array[i], array[i//3] + 1)
        if array[i] != prev :
            how[i] = i//3
    # 2 곱하기
    if i % 2 == 0 :
        prev = array[i]
        array[i] = min(array[i], array[i//2] + 1)
        if array[i] != prev :
            how[i] = i//2
    # 1 더하기
    prev = array[i]
    array[i] = min(array[i], array[i-1] + 1)
    if array[i] != prev :
        how[i] = i-1

print(array[n])

num = n
print(num, end = ' ')
while num != 1 :
    print(how[num], end = ' ')
    num = how[num]