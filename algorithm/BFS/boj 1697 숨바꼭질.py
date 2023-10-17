#백준 1697 숨바꼭질
from collections import deque

n,k = map(int,input().split())
if n==k:
    print(0)
else:
    q=deque()
    visited = [False]*100001
    visited[n]=True
    q.append((n,0))
    answer = 0
    flag = True

    while q and flag:
        n, cnt = q.popleft()
        d = [n+1,n-1,n*2]
        for i in range(3):
            dn = d[i]
            if 0<=dn<=100000:
                if visited[dn]==False:
                    if dn == k:
                        answer = cnt+1
                        flag = False
                        break
                    q.append((dn,cnt+1))
                    visited[dn] = True
    print(answer)
