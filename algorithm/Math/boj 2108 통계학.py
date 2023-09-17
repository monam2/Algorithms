#백준 2108 통계학
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
print(round(sum(arr)/len(arr)))
print(arr[len(arr)//2])

num_dict = {}

for i in arr:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1
result = []
maxV = max(num_dict.values())

for i in num_dict:
    if maxV == num_dict[i]:
        result.append(i)

if len(result) > 1:
    print(result[1])
else:
    print(result[0])

print(max(arr) - min(arr))
