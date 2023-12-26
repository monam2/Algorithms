#SWEA 두 개의 숫자열

T = int(input())
for t in range(1,1+T):
    a, b = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    long, short = 0, 0

    if a>b:
        gap = a-b
        long = a
        short = b
        long_arr = arr_a
        short_arr = arr_b
    else:
        gap = b-a
        long = b
        short = a
        long_arr = arr_b
        short_arr = arr_a
    mx = 0
    for i in range(gap+1):
        total = 0
        for j in range(short):
            total += short_arr[j]*long_arr[j+i]
        mx = max(mx, total)
    print(f"#{t} {mx}")