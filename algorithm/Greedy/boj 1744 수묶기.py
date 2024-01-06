#백준 1744 수 묶기

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

#음수가 짝수개인지 홀수개인지 체크
plus = []
minus = []
zero = []
one = []
for num in arr:
    if num > 1:
        plus.append(num)
    elif num == 1:
        one.append(num)
    elif num == 0:
        zero.append(num)
    else:
        minus.append(num)

total = 0

#1. 음수 제거
minus.sort()
if len(minus)%2==1: #음수가 홀수개
    temp = minus.pop()
    if len(zero) > 0:
        zero.pop()
    else:
        total += temp

while len(minus) > 0: #음수 제거
    a = minus.pop()
    b = minus.pop()
    total += a*b

#2. 0 제거(0이 여러개일 수도 있음)
while len(zero) > 0:
    zero.pop()

#3. 1 제거(1도 여러개일 수 있음)
while len(one) > 0:
    one.pop()
    total += 1

#4. 양수 갯수 확인
plus.sort(reverse=True)
if len(plus)%2==1:
    total += plus.pop()

while len(plus) > 0:
    a = plus.pop()
    b = plus.pop()
    total += a*b

print(total)