def solution() :
    n, m = map(int, input().split())
    parents = [i for i in range(n+1)]

    for _ in range(m) :
        cmd, a, b = map(int, input().split())
        if cmd == 0 : # 합집합
            if parents[a] > parents[b] :
                parents[b] = parents[a]
            else :
                parents[a] = parents[b]
        elif cmd == 1 : # 같은 집합인지 확인
            if parents[a] == parents[b] : 
                print("YES")
            else :
                print("NO")

solution()