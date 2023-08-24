#10815 숫자 카드

n = int(input())
sg = list(map(int, input().split()))
m = int(input())
what = list(map(int, input().split()))
dc = {}
for i in sg:
    dc[i] = True
for i in what:
    if i in dc:
        print(1, end=' ')
    else:
        print(0, end=' ')
