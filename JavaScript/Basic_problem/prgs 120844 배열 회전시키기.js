//프로그래머스 120844 배열 회전시키기
function solution(numbers, direction) {
    if (direction==='right'){
        let temp = numbers.pop();
        numbers.unshift(temp);
    } else {
        let temp = numbers.shift();
        numbers.push(temp);
    }
    return numbers;
}
