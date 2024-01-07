#백준 1715 카드 정렬하기
import heapq

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

heapq.heapify(arr)
total = 0

while len(arr) > 1:
    tmp = heapq.heappop(arr) + heapq.heappop(arr)
    heapq.heappush(arr, tmp)
    total += tmp
    
print(total)


# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))

# total = 0

# while len(arr) > 1:
#     arr.sort(reverse=True)
#     a = arr.pop()
#     b = arr.pop()
#     total += a + b
#     arr.append(a+b)
# print(total)