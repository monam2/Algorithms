# 11652 카드

from collections import defaultdict

N = int(input())
nums = {}
for i in range(N):
    n = int(input())
    if n in nums:
        nums[n] += 1
    else:
        nums[n] = 0

result = []
maxV = 0

for k, v in nums.items():
    if v == maxV:
        result.append(k)
    elif v > maxV:
        result = []
        result.append(k)
        maxV = v

result.sort()
print(result[0])
