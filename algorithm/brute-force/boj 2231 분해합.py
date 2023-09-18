#백준 2231 분해합

n = int(input())
result = []

for i in range(1,n+1):
    total = i
    arr = list(str(i))
    for j in arr:
        total += int(j)
    if total == n:
        result.append(i)
        break
else:
    print(min(result))

# #백준 2231 분해합(최대 실행)

# n = int(input())
# result = []

# for i in range(1000000):
#     total = i
#     arr = list(str(i))
#     for j in arr:
#         total += int(j)
#     if total == n:
#         result.append(i)
#         break

# if len(result)==0:
#     print(0)
# else:
#     print(min(result))

# map함수 이용 풀이
# n = int(input())
# for i in range(1,n+1):
#     a = sum(map(int, str(i)))
#     if n == i+a:
#         print(i)
#         break
# else:
#     print(0)
