n = int(input())
array = []

for _ in range(n) :
    x, y = map(int, input().split())
    array.append((x, y))


for i in array :
    x, y = i
    rank = 1
    for j in array :
        x_, y_ = j
        if x < x_ and y < y_ :
            rank += 1
    print(rank, end = ' ')
