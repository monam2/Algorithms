#swea 2817 부분 수열의 합
def dfs(index,sum_num): #총합, 노드 레벨
    global result
    if index == n:
        if sum_num == k:
            result += 1
        return
    dfs(index+1, sum_num+arr[index])
    dfs(index+1, sum_num)

T = int(input())
for t in range(1,T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    dfs(0, 0)
    print(f"#{t} {result}")