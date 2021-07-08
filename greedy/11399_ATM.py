n = int(input())
array = list(map(int, input().split()))

# 인출 시간이 짧은 순서대로 정렬
array = sorted(array)

answer = 0
wait_time = 0
for i in array :
    answer += (wait_time + i)
    wait_time += i
print(answer)
