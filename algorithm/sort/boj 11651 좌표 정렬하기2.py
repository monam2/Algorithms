#백준 11651 좌표 정렬하기2

n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x,y))

arr.sort(key=lambda s : (s[1],s[0]))
for i in range(n):
    print(*arr[i])