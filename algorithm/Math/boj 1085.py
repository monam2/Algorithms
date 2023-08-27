#1085 직사각형에서 탈출

x,y,w,h = map(int, input().split())

#1번
print(min(x, y, h-y, w-x))

#2번
# garo = 0
# sero = 0

# if x > w//2:
#     garo = w-x
# elif x < w//2:
#     garo = x
# else:
#     garo = x

# if y > h//2:
#     sero = h-y
# elif y < h//2:
#     sero = y
# else:
#     sero = y

# print(min(garo, sero))
