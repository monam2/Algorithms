# 7511 소셜 네트워킹 어플리케이션

# 유니온파인드
# union => 합치기
# find => 부모 찾기
# parent => 자기 자신을 부모로 하는 노드
# rank => 초기 높이

# x집합의 부모찾기
def find(parent, x):
    # x가 부모가 아니면 재귀 돌려서 반복
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    # 부모가 다르면 합쳐야함, 합칠때 더 큰 그래프쪽으로 합치기(rank)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

T = int(input())

for t in range(T):
    N = int(input())
    F = int(input())

    parent = list(range(N)) # 부모(루트)가 누구인지 기록하는 배열
    rank = [0] * N

    # 친구 관계 입력
    for _ in range(F):
        a, b = map(int, input().split())
        union(parent, rank, a, b)


    m = int(input())
    result = []

    for _ in range(m):
        u,v = map(int, input().split())

        # 경로 존재 => 같은 부모(같은 집합)
        if find(parent, u) == find(parent, v):
            result.append(1)
        else:
            result.append(0)

    print(f"Scenario {t+1}:")
    for r in result:
        print(r)
    print()