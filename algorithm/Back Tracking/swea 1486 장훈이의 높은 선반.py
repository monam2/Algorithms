#swea 장훈이의 높은 선반
def dfs(index, height):
    global answer
    if index == N:
        if height >= B:
            answer = min(answer, height-B)
        return

    dfs(index+1, height+arr[index])
    dfs(index+1, height)

T = int(input())
for t in range(1,1+T):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = float('inf')
    dfs(0,0)
    print(f"#{t} {answer}")