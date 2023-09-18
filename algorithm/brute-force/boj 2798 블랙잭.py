#백준 2798 블랙잭

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[i]+arr[j]+arr[k] <= m:
                result.append(arr[i]+arr[j]+arr[k])
print(max(result))
