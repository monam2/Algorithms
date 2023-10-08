//프로그래머스 120844 배열 회전시키기
function solution(numbers, direction) {
    return direction==='right' ?  [numbers.pop(), ...numbers] : [...numbers.slice(1), numbers.shift()]
} 
// ... : 배열 전개해서 새로운 배열 생성

// function solution(numbers, direction) {
//     if (direction==='right'){
//         let temp = numbers.pop();
//         numbers.unshift(temp);
//     } else {
//         let temp = numbers.shift();
//         numbers.push(temp);
//     }
//     return numbers;
// }
