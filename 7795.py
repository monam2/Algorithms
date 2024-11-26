# 7795 먹을 것인가 먹힐 것인가
from bisect import bisect_right, bisect_left

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    aList = list(map(int, input().split()))
    bList = list(map(int, input().split()))

    aList.sort()
    bList.sort()

    result = 0
    for b in bList:
        idx = bisect_right(aList, b)
        result += len(aList[idx:])

    print(result)

# 1 1 3 7 8
# 1 3 6