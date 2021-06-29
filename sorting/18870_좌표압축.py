import sys
ipt = sys.stdin.readline

n = int(ipt())
array = list(map(int, ipt().split()))
cnt_array = list(sorted(set(array)))

# 각 value의 위치 번호를 dictionary로 저장해두면 O(1)로 찾을 수 있음
cnt_array = {cnt_array[i] : i for i in range(len(cnt_array))}

for i in array :
    print(cnt_array[i], end = ' ')