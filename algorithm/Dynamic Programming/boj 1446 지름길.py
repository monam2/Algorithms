#백준 1446 지름길

n,d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dist = [i for i in range(d+1)]

for i in range(len(dist)):
    #현재 보는 칸-> 지름길통한 값, 이전칸+1 중 작은거.
    #현재 위치로 오는 지름길 없으면 이전칸+1이 됨.
    dist[i] = min(dist[i], dist[i-1]+1)

    for s,e,short in graph:
        #시작점이 현재위치인 지름길
        #끝이 범위를 벗어나지 않는 지름길
        #시작과 끝이 같은 지름길이 있을 때 더 짧으면
        if s == i and e <= d and dist[i]+short < dist[e]:
            #지금 보는 지름길을 지난 값으로 교체
            dist[e] = dist[i]+short
print(dist[d])
