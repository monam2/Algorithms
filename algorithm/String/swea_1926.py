#간단한 369게임
result = []
n = int(input())
for i in range(1, n+1):
    how = 0
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        for j in ['3','6','9']:
            how += str(i).count(j)
        result.append('-'*how)
 
 
    else:
        result.append(str(i))
print(' '.join(result))
