#swea 2805 농작물 수확하기

T = int(input())
for t in range(1,T+1):
    n = int(input())
    graph = [list(map(str, input())) for _ in range(n)]
    answer = 0
    mid = n//2
    left, right = 0, 0
    for i in range(mid):
        arr = graph[i][mid+left:mid+right+1]
        answer += sum(list(map(int, arr)))
        left -= 1
        right += 1

    for i in range(mid, n):
        arr = graph[i][mid+left:mid+right+1]
        answer += sum(list(map(int, arr)))
        left += 1
        right -= 1

    print(f"#{t}", answer)