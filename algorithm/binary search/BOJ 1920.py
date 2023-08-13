#1920 수 찾기
n = int(input())
a = list(map(int, input().split())) #반복문 돌 놈
m = int(input())
arr = list(map(int, input().split())) # 있는지 확인할 놈
a.sort()


for i in arr:
    left =0
    right = n-1
    while True:
        mid = (left+right)//2
        if left > right:
            print(0)
            break
        if a[mid] == i:
            print(1)
            break
        elif i> a[mid]:
            left = mid +1
        elif i<a[mid]:
            right = mid - 1
    
