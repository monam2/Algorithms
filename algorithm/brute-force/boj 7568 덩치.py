#7568 덩치

n = int(input())
inform = []

for _ in range(n):
    a,b = map(int,input().split())
    inform.append((a,b))

for i in inform:
    grade = 1
    for j in inform:
        if i[0]<j[0] and i[1]<j[1]:
            grade += 1
    print(grade, end=' ')

# 틀린 풀이
# result = [1]
# arr = sorted(inform)
# arr.sort(key=lambda x : (x[0],x[1]))
# arr.reverse()
# d = {}
# for i in range(len(arr)):
#     d[arr[i]] = i+1

# for i in range(1,len(arr)):
#     if arr[i-1][1] > arr[i][1]:
#         result.append(i+1)
#     elif arr[i-1][1] == arr[i][1] or arr[i-1][1] < arr[i][1]:
#         d[arr[i]] = d[arr[i-1]]

# for i in infom:
#     print(d[i], end=' ')
