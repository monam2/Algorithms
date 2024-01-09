#백준 11000 강의실 배정
#n*n으로 가면 20만이라서 시간초과남.
# -> 힙큐를 이용해서 시간복잡도 감소 시켜야함
#수업의 시작시간이 어떤 수업의 종료 시간보다 빠르다면 새로운 강의실이 필요함

import heapq, sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()
hq = []

#힙에 넣는거 : 첫 수업의 종료시간
#힙 요소와 비교하는거 : 어떤 수업의 시작 시간
heapq.heappush(hq, arr[0][1])

#힙 첫요소보다 크거나 같으면 팝 하고 추가
for i in range(1,n):
    if arr[i][0] >= hq[0]:
        heapq.heappop(hq)
    heapq.heappush(hq, arr[i][1]) #if 실행시 팝->푸시 / 실행x시 그냥 푸시

#로직 종료시 우선순위 큐의 크기 == 강의실의 갯수
print(len(hq))
