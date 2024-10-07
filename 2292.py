# 2292 벌집
# N이 1인 경우를 고려해야 함

N = int(input())

if N==1:
  print(1)
else:
  n = 1 # 껍질의 수(방)
  r = 1 # 누적 방 수

  while r < N:
    r += 6*n
    n += 1
  
  print(n)