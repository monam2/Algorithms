#백준 2960 에라토스테네스의 체

n, k = map(int, input().split())
arr = [i for i in range(2,n+1)]
result = []
i = 0
while arr:
    temp = arr[0]
    new_arr = arr[0:len(arr)]
    for j in arr:
        if j%temp==0:
            result.append(j)
            new_arr.remove(j)
    arr = new_arr

print(result[k-1])
            