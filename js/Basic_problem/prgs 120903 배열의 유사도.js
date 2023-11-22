//프로그래머스 120903 배열의 유사도
function solution(s1, s2) {
    return [...s1, ...s2].length - new Set([...s1, ...s2]).size
}
//[...s1, ...s2].length 를 s1.concat(s2).length 로 해도됨

// function solution(s1, s2) {
//     return s1.filter((v)=>s2.includes(v)).length;
// }

// function solution(s1, s2) {
//     let answer = 0;
//     for (let i =0; i<s1.length ; i++){
//         for (let j =0; j<s2.length;j++) {
//             if (s1[i]===s2[j]) {
//                 answer += 1;
//             }
//         }
//     }
//     return answer;
// }
