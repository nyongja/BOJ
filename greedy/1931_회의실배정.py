n = int(input())
array = []

for _ in range(n) :
    s, e = map(int, input().split())
    array.append((s, e))

 # 끝나는 시간을 기준으로 정렬하면 최대한 많이 회의를 할 수 있음
 # 이 때 동일한 시간에 끝나는 경우 시작 시간이 빠른 회의를 먼저 해야 함
array.sort(key = lambda x : (x[1], x[0]))

answer = 0
end_time = 0
for s, e in array :
    if s >= end_time :
        answer += 1
        end_time = e

print(answer)