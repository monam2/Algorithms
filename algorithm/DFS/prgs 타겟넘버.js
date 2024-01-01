let answer = 0;

const dfs = (numbers, target, total, idx)=>{
    if (idx == numbers.length) {
        if (total == target) answer += 1;
        return;
    }
    dfs(numbers, target, total + numbers[idx], idx + 1);
    dfs(numbers, target, total - numbers[idx], idx + 1);
}

function solution(numbers, target) {
    let total = 0;
    let idx = 0;
    
    dfs(numbers, target, total, idx);
    return answer;
}
