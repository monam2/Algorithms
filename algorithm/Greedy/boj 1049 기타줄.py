#백준 1049 기타줄

n, m = map(int, input().split())
pack = []
one = []
for i in range(m):
    a = list(map(int, input().split()))
    pack.append(a[0])
    one.append(a[1])
pack.sort()
one.sort()
if one[0]*6 < pack[0]:
    pack[0] = one[0]*6
n_div = n % 6
n = n//6
if n_div * one[0] > pack[0]:
    print((n+1)*pack[0])
else:
    print(n*pack[0] + n_div*one[0])