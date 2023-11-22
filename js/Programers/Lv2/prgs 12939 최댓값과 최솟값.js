//프로그래머스 12939 최댓값과 최솟값
function solution(s) {
    let arr = s.split(' ').map((i)=>~~i)
    let answer = [Math.min(...arr), Math.max(...arr)];
    return answer.join(' ')
}

//공백으로 구분돼서 들어옴 -> 일단 공백 기준으로 나눠야함.. 배열에 저장까지 할 수 있음.(split)
//아마 배열에 저장된건 문자열일거임. 맵핑을 통해서 정수로 바꿔야함.
//최댓값, 최솟값 각각 출력하면 될듯? 최소값 , 최대값 순으로
