#swea 1979 어디에 단어가 들어갈 수 있을까
def hang(arr):
    count = 0
    for i in range(len(arr)):
        equal = 0
        for j in range(len(arr)):
            if arr[i][j] == 1:
                equal += 1
            if arr[i][j] == 0 or j == len(arr)-1:
                if equal == k:
                    count += 1
                equal=0
    return count


T = int(input())
for tc in range(1,T+1):
    n,k = map(int,input().split())
    arr1 = []
    arr2 = []
    for i in range(n):
        inp = list(map(int, input().split()))
        arr1.append(inp)
    arr = list(zip(*arr1))
    for i in arr:
        arr2.append(list(i))
    
    a = hang(arr1)
    b = hang(arr2)
    print(f"#{tc}", a+b)
