#1051 숫자 정사각형

n,m = map(int,input().split())
arr = []
for i in range(n):
    s = list(input())
    arr.append(s)
new_arr = []
for i in arr:
    new_arr.append(list(map(int, i)))

result = 1
for k in range(n,0,-1):
    for i in range(n-k+1):
        for j in range(m-k+1):
            if arr[i][j] == arr[i][j+k-1] and arr[i][j+k-1] == arr[i+k-1][j] and arr[i+k-1][j] == arr[i+k-1][j+k-1]:
                result = max(k*k, result)
print(result)
