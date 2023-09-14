#백준 1946 신입 사원

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        a,b = map(int, input().split())
        arr.append([a,b])
    arr.sort(key = lambda v : v[0]) #서류점수 기준으로 정렬
    count = 1
    
    std = arr[0][1] #1등의 면접점수가 기준 -> 이거보다 등수가 높아야 합격
    for i in range(1,len(arr)):
        if arr[i][1] < std:
            std = arr[i][1]
            count += 1
    print(count)
