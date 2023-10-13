# 백준 9079 동전게임
from collections import deque

def make_bin(arr: list):  # 배열->2진수 생성
    a = []
    for i in arr:
        for j in i:
            a.append(j)
    n = int(''.join(map(str, a)), 2)
    return n

t = int(input())
for _ in range(t):
    input_arr = [list(map(str, input().split())) for _ in range(3)]
    # 'H' -> 1 / 'T' -> 0
    arr = []
    for k in range(3):
        new_arr = list(map(lambda v: 1 if v == 'H' else 0, input_arr[k]))
        arr.append(new_arr)

    cases = [[0, 3, 6], # 열 탐색
            [1, 4, 7],
            [2, 5, 8],
            [0, 1, 2],  # 행 탐색
            [3, 4, 5],
            [6, 7, 8],
            [2, 4, 6],  # 대각선 탐색
            [0, 4, 8]]

    visited = [False]*512
    q = deque()
    bin_n = make_bin(arr)  # 정수
    q.append((bin_n, 0))  # 배열을 2진수로 바꿔서 큐에 넣음
    visited[bin_n] = True  # 시작 노드 방문처리
    answer = -1

    while q:
        num, cnt = q.popleft()
        if num == 0 or num == 511:
            answer = cnt
            break
        for case in cases:
            b_num = list(bin(num)[2:].zfill(9))

            for c in case:
                b_num[c] = '0' if b_num[c] == '1' else '1'
            chngd_num = int(''.join(b_num), 2)

            if not visited[chngd_num]:
                visited[chngd_num] = True
                q.append((chngd_num, cnt+1))

    print(answer)
