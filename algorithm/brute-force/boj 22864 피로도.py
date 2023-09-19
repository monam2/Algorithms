#백준 22864 피로도

a,b,c,m = map(int,input().split())
task = 0
piro = 0
hour = 0

while hour < 24:
    while piro + a <= m:
        if hour > 23:
            break
        piro += a
        task += b
        hour += 1
    else:
        piro -= c
        if piro < 0:
            piro = 0
        hour += 1
print(task)
