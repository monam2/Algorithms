#swea 1961 숫자 배열 회전

T = int(input())
for t in range(1,T+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    #90도
    graph90 = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(graph[j][i])
        arr.reverse()
        graph90.append(arr)

    #180도
    graph180 = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(graph90[j][i])
        arr.reverse()
        graph180.append(arr)

    #270도
    graph270 = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(graph180[j][i])
        arr.reverse()
        graph270.append(arr)

    print(f"#{t}")
    for i in range(n):
        for j in [graph90, graph180, graph270]:
            print(''.join(map(str,j[i])), end=' ')
        print()