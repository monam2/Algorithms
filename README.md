# Code-Wallet

회원가입시 휴대폰 인증, 인증번호 생성
String(Math.floor(Math.random()*1000000)).padStart(6,'0')
-str.padStart() 
현재 문자열의 시작을 다른 문자열로 채워, 주어진 길이를 만족하는 새로운 문자열을 반환
*마스킹에도 사용 가능
const str1 = '5';

console.log(str1.padStart(2, '0'));
// Expected output: "05"

const fullNumber = '2034399002125581';
const last4Digits = fullNumber.slice(-4);
const maskedNumber = last4Digits.padStart(fullNumber.length, '*');

console.log(maskedNumber);
// Expected output: "************5581"
