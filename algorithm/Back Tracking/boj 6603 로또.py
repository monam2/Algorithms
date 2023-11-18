#백준 6603 로또
def dfs(m):
    if m==6:
        print(*s)
        return
    for i in arr:
        if visited[i]:
            continue
        if s and i < s[-1]:
            continue
        visited[i] = True
        s.append(i)
        dfs(m+1)
        s.pop()
        visited[i] = False

while True:
    arr = list(map(int, input().split()))
    k = arr.pop(0)
    if k== 0:
        break

    s=[]
    visited = [False] * 50
    dfs(0)
    print()

