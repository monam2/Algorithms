#SWEA 중간값 구하기

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[n//2])