from math import lcm

n = int(input())
array = list(map(int, input().split()))

for i in array[1:] : # 첫번째 링이 돌아갈때 나머지 돌아가는 횟수 구하려면
    m = lcm(array[0], i) # 최소공배수
    print(f'{int(m/i)}/{int(m/array[0])}') # 최소공배수를 링 크기로 나눠주기