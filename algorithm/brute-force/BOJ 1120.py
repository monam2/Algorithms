#1120 문자열

a, b = map(str, input().split())
arr = []

for i in range(len(b)-len(a)+1): #4번반복 0 1 2 3
    result = 0
    new_a = '*'*i + a + '*'*(len(b)-len(a)-i)
    for j in range(len(new_a)):
        if new_a[j]!='*' and new_a[j] != b[j]:
            result += 1
    arr.append(result)
print(min(arr))
