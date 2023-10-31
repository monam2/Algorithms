#swea 1208 flatten

for t in range(10):
    n = int(input())
    arr = list(map(int, input().split()))

    while n > 0:
        max_idx = arr.index(max(arr))
        min_idx = arr.index(min(arr))
        arr[max_idx] -= 1
        arr[min_idx] += 1
        n -= 1

    print(f"#{t+1}", max(arr) - min(arr))