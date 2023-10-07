//프로그래머스 120831 짝수의 합
const solution =(n) => {
    let arr = new Array(n).fill(0).map((_,idx)=>{return idx+1}).filter((v)=>{return v%2===0}).reduce((a,c)=>a+c,0);
    
    return arr
}

console.log(solution(10))
console.log(solution(4))

//new Array(n) : n개의 empty 배열 생성
//.fill(0) : 배열을 전부 0으로 채움(값이 있다면 수정)
//.filter(()=>{}) : {}의 조건에 맞는 것만 반환
//.reduce((a,c)=>a+c) : 합구하기. a : 이전까지 누적된 값, c : 현재값

//n이 1일 경우 문제가 생김
//n이 1이면 reduce앞에 따라 빈 배열 생성. 빈 값에 reduce를 적용하면 에러발생함. -> reduce의 초깃값 설정! : 0
