T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    s = []
    for i in range(1,n+1):
        s.append([0]*i)
        if i==1:
            s[0][0] = 1
            continue
        s[i-1][0]=1
        s[i-1][-1]=1
        if i ==2:
            continue

        for j in range(len(s[i-1])):
            if j==0 or j==len(s[i-1])-1:
                continue
            else:
                s[i-1][j] = s[i-2][j-1] + s[i-2][j]
    print(f'#{test_case}')
    for i in range(n):
        new_s = list(map(lambda x : str(x), s[i]))
        print(' '.join(new_s))
