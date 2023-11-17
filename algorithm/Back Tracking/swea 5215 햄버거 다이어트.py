#swea 5215 햄버거 다이어트

def dfs(index,score, calorie): #재료를 순회하면서 넣는 경우, 안넣는 경우 전부 탐색
    global answer
    if calorie > limit_cal:
        return
    
    answer = max(answer, score)

    if index == n: # 재료를 다 쓰면 종료
        return
    
    #재료를 쓰는 경우엔 추가해줌 
    dfs(index+1, score+mat_list[index][0], calorie+mat_list[index][1])
    #재료를 안쓰는 경우엔 순서만 넘김
    dfs(index+1, score, calorie)

T = int(input())
for t in range(1,T+1):
    n, limit_cal = map(int, input().split())
    mat_list = []
    #[(100, 200), (300, 500), (250, 300), (500, 1000), (400, 400)]
    for i in range(n):
        s, c = map(int, input().split())
        mat_list.append((s, c)) #점수, 칼로리

    dfs(0,0, 0)
    print(f"#{t} {answer}")