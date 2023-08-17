#최빈수 구하기
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    score = list(map(int, input().split()))
    maxV = []
    how = {}
    for i in range(101):
        how[i] = score.count(i)
    for v, k in how.items():
        if k == max(how.values()):
            maxV.append(v)
 
    print(f'#{test_case}', max(maxV))
