#7785 회사에 있는 사람

n= int(input())
h = set()
for i in range(n):
    s, w = input().split()
    if w =='enter':
        h.add(s)
    elif w == 'leave':
        h.remove(s)
a = sorted(list(h), reverse=True)
for i in a:
    print(i)
