#boj 17219 비밀번호 찾기

n, m = map(int, input().split())

info = {}
for i in range(n):
    url, pw = map(str, input().split())
    info[url] = pw
for j in range(m):
    what = input()
    print(info[what])