//백준 2747 피보나치 수
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
let n = +input[0];

function fibo(n) {
  let arr = [0, 1];
  for (let i = 0; i < n - 1; i++) {
    let len = arr.length;
    arr.push(arr[len - 1] + arr[len - 2]);
  }
  return arr[n];
}

console.log(fibo(n));
