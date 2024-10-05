# 1992 쿼드 트리

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

depth = {}
for i in range(8):
  depth[i] = []

def seperate(n, x, y):
  
  total = 0
  for i in range(x, x+n):
    for j in range(y, y+n):
      total += graph[i][j]
  
  if total == n*n:
    return '1'
  elif total == 0:
    return '0'
  
  half = n//2
  tl = seperate(half, x, y)
  tr = seperate(half, x, y+half)
  bl = seperate(half, x+half, y)
  br = seperate(half, x+half, y+half)
  return '(' + tl + tr + bl + br + ')'

print(seperate(N, 0, 0))