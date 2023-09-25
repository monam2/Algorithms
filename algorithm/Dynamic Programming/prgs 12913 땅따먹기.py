#프로그래머스 땅따먹기
# def solution(land):
#     maxV = max(land[0])
#     idx = land[0].index(maxV)
#     for i in range(1, len(land)):
#         for j in range(4):
#             if j!=idx:
#                 land[i][j] += maxV
#             elif j==idx:
#                 land[i][j] = 0
#         maxV = max(land[i][0],land[i][1],land[i][2],land[i][3])
#         idx = land[i].index(maxV)
#     return maxV
        

# def solution(land):
#     land.append([0,0,0,0])
#     answer = 0
#     for i in range(len(land)-1):
#         answer += max(land[i])
#         land[i+1][land[i].index((max(land[i])))] = 0

#     return answer

# def solution(land):
#     land.append([0,0,0,0])
#     beforeMax = 0
#     maxV = 0
#     for i in range(len(land)-1):
#         dp = [0]*4
#         maxV = max(land[i])
#         for j in range(4):
#             if land[i][j] == maxV:
#                 dp[j] = maxV
#                 dp[j] += beforeMax
#                 land[i+1][j] = 0
#                 beforeMax = dp[j]
#     return max(dp)

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
