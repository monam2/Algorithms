#백준 14888 연산자 끼워넣기

#최댓값 구하기
def mmax(idx,plus,minus,mul,div,total):
    global max_res
    max_res = max(max_res, total)
    if idx == n:
        return

    if plus > 0:
        mmax(idx+1,plus-1,minus,mul,div,total+num[idx])
    if minus > 0:
        mmax(idx+1,plus,minus-1,mul,div,total-num[idx])
    if mul > 0:
        mmax(idx+1,plus,minus,mul-1,div,total*num[idx])
    if div > 0:
        mmax(idx+1,plus-1,minus,mul,div-1,total//num[idx])

#최솟값 구하기
def mmin(idx,plus,minus,mul,div,total):
    global min_res
    min_res = min(min_res, total)
    if idx == n:
        return
    if plus > 0:
        mmin(idx+1,plus-1,minus,mul,div,total+num[idx])
    if minus > 0:
        mmin(idx+1,plus,minus-1,mul,div,total-num[idx])
    if mul > 0:
        mmin(idx+1,plus,minus,mul-1,div,total*num[idx])
    if div > 0:
        mmin(idx+1,plus-1,minus,mul,div-1,total//num[idx])

n = int(input())
num = list(map(int, input().split()))
plus,minus,mul,div = map(int, input().split())
idx = 1
total = num[0]
max_res = 0
min_res = float('inf')

mmax(idx,plus,minus,mul,div,total)
mmin(idx,plus,minus,mul,div,total)

print(max_res)
print(min_res)