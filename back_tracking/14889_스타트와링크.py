n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

answer = int(1e9)

def score(team) : # 팀원 점수 계산
    score = 0 
    for i in range(len(team) - 1) :
        for j in range(i, len(team)) :
            score += array[team[i]][team[j]]
            score += array[team[j]][team[i]]
    return score

def dfs(x, start, link) :
    global answer
    if x == n : 
        if len(start) != len(link) : # 팀원 수가 같아야 함
            return
        s_score = score(start)
        l_score = score(link)
        diff = abs(s_score - l_score)
        answer = min(diff, answer)
        return
    else :
        # 1) start 팀에 넣기
        start.append(x)
        dfs(x+1, start, link)
        start.pop()
        # 2) link 팀에 넣기
        link.append(x)
        dfs(x+1, start, link)
        link.pop()

dfs(0, [], [])
print(answer)