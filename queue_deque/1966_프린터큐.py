from collections import deque

t = int(input())

for _ in range(t) :
    n, m = map(int, input().split()) # n : 문서의 개수, m : 순서 확인하고 싶은 문서 인덱스
    printer = deque()
    doc_lst = list(map(int, input().split()))
    importance = list()
    
    for i, imp in enumerate(doc_lst) :
        printer.append((imp, i)) # (문서 중요도, 인덱스)
        importance.append(imp)
    importance.sort()
    
    idx = -1
    answer = 1
    while idx != m :
        v, i = printer.popleft()
        if v == importance[-1] and i == m :
            idx = i
        elif v == importance[-1] :
            answer += 1
            importance.pop()
        else :
            printer.append((v, i))
    print(answer)