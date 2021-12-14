import sys
input = sys.stdin.readline
T = int(input()) # 테스트 케이스 수

for _ in range(T) :
    n, m = map(int, input().split()) # 국가의 수, 비행기의 종류

    for _ in range(m) :
        _, _ = map(int, input().split()) # a <-> b 왕복 비행기 
    
    print(n-1)