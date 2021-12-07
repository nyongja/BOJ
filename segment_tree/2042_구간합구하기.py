def init(start, end, node) :
    if start == end :
        tree[node] = array[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]

# start, end : 시작 / 끝 인덱스
# left, right : 구간 합을 구하고자하는 범위
def sum(start, end, node, left, right) :
    # 범위 밖에 있는 경우
    if left > end or right < start :
        return 0
    # 범위 안에 있는 경우 
    if left <= start and end <= right :
        return tree[node]
    mid = (start + end) // 2
    return sum(start, mid, node*2, left, right) + sum(mid + 1, end, node*2+1, left, right)

n, m = map(int, input().split())
array = list(map(int, input().split()))
tree = [0] * (4*n)
init(0, len(array)-1, 1)

for _ in range(m) :
    i, j = map(int, input().split())
    print(sum(0, len(tree), 1, i, j))