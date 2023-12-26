#백준 14888 연산자 끼워넣기

def maxmin(idx,plus,minus,mul,div,total):
    global max_res, min_res
    if idx == n:
        max_res = max(max_res, total)
        min_res = min(min_res, total)
        return

    if plus > 0:
        maxmin(idx+1,plus-1,minus,mul,div,total+num[idx])
    if minus > 0:
        maxmin(idx+1,plus,minus-1,mul,div,total-num[idx])
    if mul > 0:
        maxmin(idx+1,plus,minus,mul-1,div,total*num[idx])
    if div > 0:
        maxmin(idx+1,plus,minus,mul,div-1,int(total/num[idx]))

n = int(input())
num = list(map(int, input().split()))
plus,minus,mul,div = map(int, input().split())
idx = 1
total = num[0]
max_res = -1000000000
min_res = 1000000000

maxmin(idx,plus,minus,mul,div,total)

print(max_res)
print(min_res)