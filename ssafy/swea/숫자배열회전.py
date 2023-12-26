#SWEA 숫자배열회전
#전치행렬 -> 리버스 : 시계방향 90도 회전
T = int(input())
for t in range(1,T+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    #90도 회전
    graph1 = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(graph[j][i])
        arr.reverse()
        graph1.append(arr)

    # +90
    graph2 = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(graph1[j][i])
        arr.reverse()
        graph2.append(arr)

    # +90
    graph3 = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(graph2[j][i])
        arr.reverse()
        graph3.append(arr)

    print(f"#{t}")
    for i in range(n):
        print(''.join(list(map(str, graph1[i]))), ''.join(list(map(str, graph2[i]))), ''.join(list(map(str, graph3[i]))))