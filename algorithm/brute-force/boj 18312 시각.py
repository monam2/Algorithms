#백준 18312 시각
n,k = map(int,input().split())
count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            a = [h,m,s]
            newa = []
            for i in a:
                if i//10 == 0:
                    i = '0'+str(i)
                else:
                    i = str(i)
                newa.append(i)

            for i in newa:
                if i.count(str(k)) > 0:
                    count += 1
                    break
print(count)
