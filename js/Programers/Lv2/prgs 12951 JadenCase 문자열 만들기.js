//프로그래머스 12951 JadenCase 문자열 만들기
function solution(s) {
    let arr = s.split(' ').map((value)=>{
        if (value) {return value[0].toUpperCase() + value.slice(1).toLowerCase()}
    })
    let answer;
    answer = arr.join(' ');
    return answer;
}


/**
공백에 따라서 나눠서 볼건데, 공백이 연속해서 나올 수 있음.
**/
