# 11286 절댓값 힙
import heapq

N = int(input())

heap = []
result = []

for _ in range(N):
    n = int(input())

    if n != 0:
        heapq.heappush(heap, (abs(n), n))
    else:
        if heap:
            p = heapq.heappop(heap)
            result.append(p[1])
        else:
            result.append(0)

for num in result:
    print(num)
