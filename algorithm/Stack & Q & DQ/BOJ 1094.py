#1094 막대기
long = [64]
n = int(input())
while True:
    if sum(long) == n:
        break
    elif sum(long) > n:
        a = long.pop()//2
        long.append(a)
        if sum(long) < n:
            long.append(a)
print(len(long))
