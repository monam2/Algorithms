# 10816 숫자 카드 2

_ = int(input())
nArr = list(map(int, input().split()))
_ = int(input())
mArr = list(map(int, input().split()))

dict = {}
for n in nArr:
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1

result = [dict.get(m, 0) for m in mArr]
print(*result)