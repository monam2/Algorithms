from collections import deque

# 입력 받기
C, B = map(int, input().split())

# 브라운의 이동 방향
BROWN_MOVE = [-1, 1, 2]

# BFS 큐 초기화
q = deque()
q.append((B, 0))  # (브라운 위치, 시간)

# 방문 체크 리스트
visited = [False] * 200001

# 결과 초기화
result = -1

# BFS 탐색 시작
while q:
    # 현재 큐의 사이즈를 기준으로 BFS 진행
    for _ in range(len(q)):
        now_pos, now_time = q.popleft()

        # 현재 시간에 코니의 위치 계산
        current_c = C + (now_time * (now_time + 1)) // 2

        # 코니가 범위를 벗어나면 종료
        if current_c > 200000:
            break

        # 브라운이 코니를 잡았다면 종료
        if now_pos == current_c:
            result = now_time
            q.clear()  # 큐를 비워서 루프 종료
            break

        # 브라운의 이동
        for d in BROWN_MOVE:
            if d == 2:
                new_pos = now_pos * 2
            else:
                new_pos = now_pos + d

            # 새로운 위치가 유효하고 방문하지 않은 경우
            if 0 <= new_pos <= 200000 and not visited[new_pos]:
                visited[new_pos] = True
                q.append((new_pos, now_time + 1))

    if result != -1:
        break

# 결과 출력
print(result)
