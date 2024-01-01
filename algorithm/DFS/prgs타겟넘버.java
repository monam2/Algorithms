class Solution {
    int answer = 0;
    public void dfs(int[] numbers, int target, int total, int idx) {
        if (idx == numbers.length) {
            if (total == target) answer += 1;
            return;
        }
        
        dfs(numbers, target, total + numbers[idx], idx + 1);
        dfs(numbers, target, total - numbers[idx], idx + 1);
    }
    
    public int solution(int[] numbers, int target) {
        int total = 0;
        int idx = 0;
        
        dfs(numbers, target, total, idx);
        return answer;
    }
}
