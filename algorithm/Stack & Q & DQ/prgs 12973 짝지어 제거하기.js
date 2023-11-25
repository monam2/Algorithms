function solution(s)
{
    s=s.split('');
    let stack = [];
    for (let i=0;i<s.length;i++){
        if (stack && stack[stack.length-1]===s[i]) {
            stack.pop();
        } else {
            stack.push(s[i]);
        }
    }
    if (stack.length===0) return 1;
    else return 0;
    
    //시간초과 코드
    // s = s.split('');
    // while (s.length>0) {
    //     let pair = false;
    //     for (let i=0; i<s.length-1; i++) {
    //         if (s[i] === s[i + 1]) {
    //             s.splice(i, 2); //splice는 원본배열을 수정
    //             pair = true;
    //             break;
    //         }
    //     } 
    //     if (!pair) return 0 //for문이 다 끝났을 때 false이면 0
    // }
    // return 1 //s가 0이 돼서 정상 종료 -> 1
}
