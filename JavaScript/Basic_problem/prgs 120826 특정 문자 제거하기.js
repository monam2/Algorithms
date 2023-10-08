//프로그래머스 120826 특정 문자 제거하기

//문자열.repalceAll(바꿀항목, 뭐라고 바꿀지)
function solution(my_string, letter) {
    return my_string.replaceAll(letter, "");
}

// function solution(my_string, letter) {
//     return my_string.split('').filter((v)=>{return v!==letter}).join('');
// }
