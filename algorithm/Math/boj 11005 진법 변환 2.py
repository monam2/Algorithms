#백준 11005 진법 변환2

n,b = map(int, input().split())
result = ""
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while n!=0:
    result = arr[n % b] + result
    n//=b

print(result)