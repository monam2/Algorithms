#1004 어린왕자

t = int(input())
for test_case in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for i in range(n):
        cx, cy, cr = map(int,input().split())
        d1 = ((x1-cx)**2 + (y1-cy)**2)**(1/2)
        d2 = ((x2-cx)**2 + (y2-cy)**2)**(1/2)
        if d1>cr and d2>cr:
            continue
        elif d1<cr and d2<cr:
            continue
        elif d1>cr or d2>cr:
            count += 1
    print(count)
