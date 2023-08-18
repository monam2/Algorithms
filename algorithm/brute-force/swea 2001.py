#  swea 2001 파리퇴치
T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    result = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            all = 0
            for x in range(i, i+m):
                for y in range(j,j+m):
                    all += arr[x][y]
            result = max(result, all)
    print(f'#{test_case}', result)
