#swea 1222 계산기1

for t in range(10):
    n = int(input())
    arr = list(map(int, input().split('+')))
    print(f"#{t+1}",sum(arr))
