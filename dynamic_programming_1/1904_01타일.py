n = int(input())
array = [0]
array.append(1)
array.append(2)

# 점화식의 특성 상
# 이전 값의 앞부분에만 1을 붙이고
# 이전이전 값의 뒷부분에만 00을 붙이면 중복 없이 구할 수 있음

for i in range(3, n + 1) :
    array.append((array[i-1] + array[i-2]) % 15746)

print(array[n])
