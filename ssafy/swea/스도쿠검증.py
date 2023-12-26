#swea 스도쿠검증

#가로 | 세로 | 1/9칸 -> 1-9까지 전부 있는지 검증 -> hash

def garo(graph):
    for i in range(9):
        garo_n = {1:True, 2: True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True}
        for j in range(9):
            if garo_n[graph[i][j]] == True:
                garo_n[graph[i][j]] = False
        if True in list(garo_n.values()):
            return False
    return True

def sero(graph):
    for i in range(9):
        sero_n = {1:True, 2: True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True}
        for j in range(9):
            if sero_n[graph[j][i]] == True:
                sero_n[graph[j][i]] = False
        if True in list(sero_n.values()):
            return False
    return True

def cross(graph):
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            cr_n = {1:True, 2: True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True}
            for q in range(i,i+3):
                for w in range(j, j+3):
                    if cr_n[graph[q][w]] == True:
                        cr_n[graph[q][w]] = False
        if True in list(cr_n.values()):
            return False
    return True


T = int(input())
for t in range(1,T+1):
    graph = [list(map(int, input().split())) for _ in range(9)]
    answer = 0
    g,s,c = False, False, False
    #가로
    g = garo(graph)
    #세로 -> 가로가 참이면 수행
    if g:
        s = sero(graph)

    if g and s:
        c = cross(graph)

    if c:
        answer = 1
    
    print(f"#{t} {answer}")