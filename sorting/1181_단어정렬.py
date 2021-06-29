import sys

def setting(data) :
    return len(data)

ipt = sys.stdin.readline
n = int(ipt())
array = []

for _ in range(n) :
    array.append(ipt()[:-1])

array = list(set(array)) # 중복 제거
array = sorted(array) # 알파벳 순 정렬
array = sorted(array, key = setting) # 길이 별 정렬

for i in array :
    print(i) 
