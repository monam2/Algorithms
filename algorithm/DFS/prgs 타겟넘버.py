def dfs(numbers, target, total, idx):
    global answer
    if idx == len(numbers):
        if total == target:
            answer += 1
        return
    
    dfs(numbers, target, total + numbers[idx], idx + 1)
    dfs(numbers, target, total - numbers[idx], idx + 1)
        
answer = 0

def solution(numbers, target):
    global answer
    idx = 0
    total = 0
    
    result = dfs(numbers, target, total, idx)
    
    return answer
