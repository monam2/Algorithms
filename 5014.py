# 5014 스타트와 링크
from collections import deque


def bfs(F, S, G):
    visited = [False for _ in range(F + 1)]
    quuu = deque()

    quuu.append([S, 0])
    visited[S] = True

    while quuu:
        now, cnt = quuu.popleft()

        if now == G:
            return cnt

        for mv in MOVEMENT:
            ns = now + mv

            if 0 < ns <= F and not visited[ns]:
                quuu.append([ns, cnt + 1])
                visited[ns] = True
    return "use the stairs"


F, S, G, U, D = map(int, input().split())

MOVEMENT = [U, -D]

print(bfs(F, S, G))
