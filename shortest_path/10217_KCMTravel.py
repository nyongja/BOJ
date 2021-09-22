import sys
input = sys.stdin.readline

INF = sys.maxsize

T = int(input()) # 테스트케이스
for _ in range(T) :
    n, m, k = map(int, input().split()) # 공항의 수, 총 지원비용, 티켓정보의 수
    graph = [[] for _ in range(n+1)]
    for _ in range(k) :
        u, v, c, d = map(int, input().split()) # u -> v 로가는 비용 c, 소요시간 d
        graph[u].append((v, c, d))
    dp = [[INF]*(m+1) for _ in range(n+1)]

    dp[1][0] = 0

    for cost in range(m+1) :
        for airport in range(1, n+1) :
            if dp[airport][cost] == INF : # cost로 airport에 도착하는 경우가 없으면
                continue
            time = dp[airport][cost] # airtport까지 cost로 도착할때까지 걸리는 소요 시간
            for nairport, ncost, ntime in graph[airport] : # airport에서 출발해서 다음 장소까지 걸리는 티켓들
                if cost + ncost > m : # 주어진 비용을 초과하면
                    continue
                dp[nairport][cost+ncost] = min(dp[nairport][cost+ncost], time + ntime)
    print("dp : ", dp)
    if min(dp[-1]) == INF :
        print("Poor KCM")
    else : print(min(dp[-1]))