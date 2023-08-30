#1932 정수삼각형

def solution(arr):
    for i in range(1,len(arr)):
        for j in range(i+1):
            if j == 0:
                arr[i][j] += arr[i-1][j]
            elif i == j:
                arr[i][j] += arr[i-1][j-1]
            else:
                arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])
    return max(arr[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
