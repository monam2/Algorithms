#프로그래머스 프렌즈4블록

def solution(m, n, board):
    arr = [] #전치행렬 arr 생성
    for i in range(n):
        a = []
        for j in range(m):
            a.append(board[j][i])
        a.reverse() #내려오는 방향을 배열과동일시하기 위해 행렬 좌우반전
        arr.append(a)

    count = 0
    while True:
        will_rm = []
        for i in range(n-1): #완전탐색 후 remove배열에 같은 쌍 넣기
            for j in range(m-1):
                if arr[i][j]==arr[i+1][j]==arr[i][j+1]==arr[i+1][j+1] and arr[i][j] != 'X':
                    will_rm.append([i,j]) #X는 이미 제거된 블록이므로 제외
                    will_rm.append([i,j+1])
                    will_rm.append([i+1,j])
                    will_rm.append([i+1,j+1])
        if len(will_rm)==0: #같은 쌍이 없으면 종료
            return count
        
        for x,y in will_rm: #같은쌍 X로 변경, 중복은 pass함.
            if arr[x][y]!='X':
                arr[x][y]='X'
                count += 1
        for i in range(n-1,-1,-1): #역순으로(밑에서부터&우측에서부터)
            for j in range(m-1,-1,-1): #X를 빼서 뒤로 append
                if arr[i][j]=='X':
                    arr[i].pop(j)
                    arr[i].append('X')

print(solution(4,5,	["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
