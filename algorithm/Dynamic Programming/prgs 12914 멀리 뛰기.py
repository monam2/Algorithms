#프로그래머스 12914 멀리 뛰기
def solution(n):
    dp = [0]*2001
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(2,n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]%1234567
  
print(solution(4))
print(solution(3))

# from itertools import permutations
# from collections import deque
# def solution(n):
#     answer = 0
#     if n%2==0: #even
#         for i in range((n//2)+1):
#             if i==0 or i==(n//2):
#                 answer += 1
#             else:
#                 arr = deque([1]*n)
#                 for j in range(i):
#                     arr.popleft()
#                     arr.popleft()
#                     arr.append(2)
#                 answer += len(set(permutations(arr,n-i)))
#     else: #odd
#         for i in range((n//2)+1):
#             if i==0:
#                 answer += 1
#             else:
#                 arr = deque([1]*n)
#                 for j in range(i):
#                     arr.popleft()
#                     arr.popleft()
#                     arr.append(2)
#                 answer += len(set(permutations(arr,n-i)))
#     return answer%1234567

