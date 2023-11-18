#백준 2758 로또
#이전에 고른 수의 2배보다 이상만 고른다.

#dfs로 풀면 시간초과
# DP로 풀어야 할듯.
# 다시 풀기!

# def dfs(k,before):
#     global result
#     if k==n:
#         result += 1
#         return
#     for i in range(1,m+1):
#         if visited[i]: #이미 사용한건 패스
#             continue
#         if i >= before*2:
#             visited[i] = True
#             dfs(k+1, i)
#             visited[i] = False

import sys
input = sys.stdin.readline
T = int(input())
for t in range(1,T+1):
    n, m = map(int, input().split())
    # visited = [False] * 2001
    visited = [0] * 2001
    result = 0
    # dfs(0,0)

    before = 0
    visited[0] = 1
    for i in range(1,m+1):
        if i == 1:
            visited[i] = 1
        else:
            visited[i] = visited[before] * 2

    print(result)