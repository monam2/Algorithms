from collections import deque

def BFS(home):
    q = deque()
    q.append(0)
    L = 0
    ch = [0]*10001
    ch[0] = 1
    while q:
        n = len(q)
        for i in range(n):
            x = q.popleft()
            for nx in [x-1, x+1, x+5]:
                if nx >= 0 and nx <= 10000 and ch[nx]== 0:
                    q.append(nx)
                    ch[nx] = 1
                if nx == home:
                    return L + 1
        L += 1

def solution(home):
    answer = BFS(home)
    
    return answer


print(solution(10))
print(solution(14))
print(solution(25))
print(solution(24))
print(solution(345))

'''
최소 점프
현수는 놀이터에서 놀다가 집으로 가려고 합니다. 놀이터의 위치와 집의 위치가 수직선상의
좌표 점으로 주어집니다. 놀이터는 수직선상의 0지점입니다.
현수는 놀이터에서 스카이콩콩을 타고 점프를 하면서 집으로 이동하려고 합니다.
점프는 다음과 같은 규칙으로 합니다.
1) 현재 지점에서 앞으로 +1 만큼 점프이동할 수 있습니다.
2) 현재 지점에서 뒤쪽으로 -1 만큼 점프이동할 수 있습니다.
3) 현재 지점에서 앞쪽으로 +5 만큼 긴 점프이동을 할 수있습니다.
매개변수 home에 현수의 집의 위치가 주어지면 놀이터에서 집까지 최소 몇 번의 점프로 집에
도착할 수 있는지 최소 점프횟수를 구하여 반환하세요.
입출력 예:
제한사항:
• 수직선의 좌표는 0부터 10,000까지입니다.
• 현수가 집으로 반드시 갈 수 있습니다.
'''
