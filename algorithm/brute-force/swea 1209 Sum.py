#SWEA 1209 Sum
for t in range(10):
    n = int(input())
    answer = []
    graph = []
    #입력과 동시에 행 체크
    for i in range(100):
        arr = list(map(int, input().split()))
        answer.append(sum(arr))
        graph.append(arr)

    #열 체크
    for i in range(100):
        col = 0
        for j in range(100):
            col += graph[j][i]
        answer.append(col)

    #왼쪽 대각선
    left = 0
    for i in range(100):
        left += graph[i][i]
    answer.append(left)

    #오른쪽 대각선
    right = 0
    for i in range(100):
        right += graph[i][99-i]
    answer.append(right)

    print(f"#{t+1}", max(answer))
