#11478 서로 다른 부분 문자열의 개수

s = input()
a = set()
for i in range(1,len(s)+1):
    for j in range(len(s)-i+1):
        result = s[j:j+i]
        a.add(result)
print(len(a))
