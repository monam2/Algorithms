#SWEA 1220 Magnetic
from collections import deque

for t in range(10):
    answer = 0
    n = int(input()) 
    graph = [[] for _ in range(100)] #2차원 배열을 입력받아서 0 제거 후 전치행렬 변환
    for i in range(100):
        arr = list(map(int, input().split()))
        for j in range(100):
            if arr[j] == 2:
                graph[j].append(2)
            elif arr[j] == 1:
                graph[j].append(1)

    new_graph = []
    for i in range(100):
        q = deque(graph[i])
        while True: #1은 오른쪽으로, 2은 왼쪽으로 끌림
            if q[-1] == 1: #배열 오른쪽에 1이 있으면 전부 제거
                q.pop()
            if q[0] == 2: #배열 왼쪽에 2이 있으면 전부 제거
                q.popleft()
            if q[0]==1 and q[-1]==2: #더이상 문제 없으면 종료
                new_graph.append(list(q))
                break

    for i in range(100): #1과 2를 짝 맞춰서 제거하기 ( 1을 기준으로 )
        stack = [1] #배열의 시작은 무조건 1임
        for j in range(1,len(new_graph[i])):
            #스택에는 1만 쌓으면 됨(이진 분류). 현재값이 1이면 append / 현재값이 2면 스택비우기
            if new_graph[i][j] == 1:
                stack.append(1)
            elif stack and new_graph[i][j] == 2:
                stack = []
                answer += 1

    print(f"#{t+1}", answer)
