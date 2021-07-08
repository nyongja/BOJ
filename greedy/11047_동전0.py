n, k = map(int, input().split())
array = []

for _ in range(n) :
  array.append(int(input()))
  
answer = 0
for i in range(n-1, -1, -1) :
  if array[i] <= k : # 단위가 큰 동전부터 가능한한 최대한 사용해서 만들기
    answer += k // array[i]
    k %= array[i]
  if k == 0 :
    break
print(answer)