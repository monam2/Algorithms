function solution(num_list) {
    let answer = [0,0];
    for (value of num_list) {
        answer[value%2] += 1
    }
    return answer
}
