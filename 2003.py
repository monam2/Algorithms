# 2003 수들의 합 2
# 수열에서 연속된 부분의 합이 M이 되는 경우
# i와 j가 같을 수도 있다

def get_sum(n, m):

  s, e = 0, 0
  ans = 0
  point_sum = 0

  while e < n:

    # 누적합이 적으면 오른쪽을 늘림
    if point_sum < m:
      point_sum += arr[e]
      e += 1

    # 누적합이 m과 같으면 정답 처리 후 
    elif point_sum == m:
      ans += 1
      point_sum += arr[e]
      e += 1
    # 누적합이 m보다 크면 왼쪽걸 빼야 함 
    else:
      point_sum -= arr[s]
      s += 1
      
  # 마지막 구간 처리해야 함 : s는 중간인데 e가 끝에 닿은 경우,
  # s만 오른쪽으로 움직이면서 마지막도 체크해야 함
  while s < n:
    if point_sum == m:
      ans += 1
    point_sum -= arr[s]
    s += 1

  return ans

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 길이를 늘려가면서 완탐을 할 수도 있고, -> 시간 제한에 걸림
# 슬라이딩 윈도우?

print(get_sum(N, M))