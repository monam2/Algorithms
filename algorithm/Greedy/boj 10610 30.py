#10610 30
n = input()

sum_n = 0
arr = []
answer = -1

if '0' in n:
    for i in n:
        sum_n += int(i)
        arr.append(i)
    if sum_n % 3 == 0:
        arr.sort(reverse=True)
        answer = ''.join(arr)

print(answer)
