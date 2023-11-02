#백준 15649 n과 m
#1부터 n까지의 자연수 중에서 중복 없이 m개를 고른 수열
def func():
    if len(s) == m: #자릿수가 다 찼으면 return 해서 부모노드로 돌아감
        print(' '.join(map(str, s)))
        return
    for i in range(1,n+1): #자릿수가 아직 안찼으면
        if visited[i] == True: #이미 사용한 수는 건너뜀(1 썼으면 다음 2, 2도 썼으면 다음 3)
            continue
        visited[i] = True #수 사용처리
        s.append(i) #수열에 수 넣음
        func()
        s.pop()
        visited[i] = False #방금 사용한 수 빼기

n,m = map(int, input().split())
s = []
visited = [False]*(n+1)
func()