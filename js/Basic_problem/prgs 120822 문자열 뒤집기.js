// function solution(my_string) {
//     return my_string.split('').reverse().join('');
// }

function solution(my_string) {
    return Array.from(my_string).reverse().join('');
}

// Array.from(객체,콜백함수) :  객체로부터 배열 생성(문자열이면 split('')이랑 같음. 콜백함수를 통해서 map처럼 기능 ex) Array.from([1,2,3], (x)=>x*2);  : [2,4,6]
