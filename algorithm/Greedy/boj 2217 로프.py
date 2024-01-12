n = int(input())

rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
result = []
for i in range(n):
    result.append(rope[i]*(i+1))
print(max(result))
'''
30 27 25 15

1개 -> 30
2개 -> 27*2
3개 -> 25*3
4개 -> 15*4
'''
