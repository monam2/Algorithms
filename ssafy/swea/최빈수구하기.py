#SWEA 최빈수 구하기

T = int(input())
for _ in range(1,T+1):
    t = int(input())
    arr = list(map(int,input().split()))
    cnt = {}
    for i in arr:
        if cnt.get(i,False):
            cnt[i] += 1
        else:
            cnt[i] = 1
    mx = max(cnt.values())
    result = 0
    for k,v in cnt.items():
        if v == mx:
            result = max(result, k)
    print(f"#{t} {result}")