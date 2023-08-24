#10816 숫자 카드 2
from collections import Counter

n = int(input())
sg = list(map(int, input().split()))
dc = Counter(sg)

m = int(input())
what = list(map(int, input().split()))
for i in what:
    if i in dc:
        print(dc[i], end=' ')
    else:
        print(0, end=' ')
