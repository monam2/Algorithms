#백준 1759 암호만들기
#최소 한 개의 모음 + 최소 두 개의 자음
#일단 알파벳 사전순 정렬
#백트래킹 -> 가지치기 조건 :앞 글자보다 현재 글자가 크면 컨티뉴 -> 이전 알바벳보다 현재 알파벳이 커야함.
def dfs(k,m,j): #노드, 모음, 자음
    if k==l:
        if m<1 or j <2:
            return
        print(''.join(letter))
        return
    for i in arr:
        if visited[i] == True:
            continue
        if letter and letter[-1] >= i:
            continue
        visited[i] = True
        letter.append(i)
        if i in mo: #모음이라면
            dfs(k+1, m+1, j)
        else: #자음이라면
            dfs(k+1, m, j+1)
        letter.pop()
        visited[i] = False
#자음? 모음?

import sys
input = sys.stdin.readline
l, c = map(int, input().split())
arr = list(map(str, input().split())) # a t c i s w
arr.sort()
mo = ['a', 'e', 'i', 'o', 'u']
count_mo, count_ja = 0,0

letter = []
visited = {}

for i in arr:
    visited[i] = False

dfs(0,0,0) #노드, 모음, 자음