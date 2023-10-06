function solution(num1, num2) {
    var answer = ~~Math.floor(num1/num2);
    return answer;
}

//풀이 방법은 세 가지
//1. 정수만 뽑아오거나(parseInt)
//2. 소수점을 버리거나(Math.floor)
//3. 비트부정연산자 (~~)
