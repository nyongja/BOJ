n = int(input())
array = []

for _ in range(n) :
    array.append(list(map(int, input().split())))

for i in range(2, n+1) :
    for j in range(len(array[n-i])) :
        array[n-i][j] += max(array[n-i+1][j], array[n-i+1][j+1]) # 밑에서부터 하나씩 계산해서 올라오기

print(array[0][0])