#백준 11497 통나무 건너뛰기

t = int(input())
for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    gap = 0
    for i in range(n-2):
        if abs(arr[i]-arr[i+2]) > gap:
            gap = abs(arr[i]-arr[i+2])
    print(gap)