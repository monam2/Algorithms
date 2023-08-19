#1057 토너먼트
n, a, b = map(int,input().split())
count = 0
while True:
    count += 1
    a = (a+1)//2
    b = (b+1)//2
    if a==b:
        break
print(count)
