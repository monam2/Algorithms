#14425 문자열 집합

n, m = map(int, input().split())
one = set()
for i in range(n):
    one.add(input())

count = 0
for i in range(m):
    if input() in one:
        count += 1
print(count)
