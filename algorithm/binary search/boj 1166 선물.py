#백준 1166 선물

n,l,w,h = map(int, input().split())
left = 0
right = max(l,w,h)


for i in range(100):
    mid = (left +right)/2

    total = (l//mid) * (w//mid) * (h//mid)
    if total >= n:
        left = mid
    else:
        right = mid
print(left)
