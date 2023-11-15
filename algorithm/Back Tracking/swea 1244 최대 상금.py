#swea 1244 최대 상금
def find(k):
    global v
    if k == n:
        v = max(v, int(''.join(map(str,s))))
        return
    for i in range(L-1):
        for j in range(i+1, L):
            s[i], s[j] = s[j], s[i]
            check = int(''.join(map(str,s)))*100 + k
            if check not in visited:
                find(k+1)
                visited.append(check)
                #재귀 이후에 방문처리하는 이유 -> 값을 전부 완성하고, 이 값(ex 88832)에 대한 재 방문을 막기 위함
            s[i], s[j] = s[j], s[i]

T = int(input())
for t in range(1,T+1):
    s, n = map(str, input().split())
    n = int(n)
    s = list(map(int, list(s)))
    L = len(s)
    visited = []
    v = 0
    find(0)
    print(f"#{t} {v}")