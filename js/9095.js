// 9095 1,2,3 더하기
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

T = input.shift();

const dp = Array.from({ length: 12 }).fill(0);
dp[0] = 0;
dp[1] = 1;
dp[2] = 2;
dp[3] = 4;
for (let i = 4; i < dp.length - 1; i++) {
  dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
}

for (t of input) {
  console.log(dp[t]);
}

/**
 * 1 = 1 -> 1
 * 2 = 1 + 1 -> 2
 *     2
 * 3 = 1 + 1 + 1 -> 4
 *     1 + 2
 *     2 + 1
 *     3
 * 4 = 1 + 1 + 1 + 1 -> 7
 *     1 + 1 + 2
 *     1 + 2 + 1
 *     2 + 1 + 1
 *     1 + 3
 *     3 + 1
 *     2 + 2
 * 5 = 1 + 1 + 1 + 1 + 1 -> 13
 *     1 + 1 + 1 + 2
 *     1 + 1 + 2 + 1
 *     1 + 2 + 1 + 1
 *     2 + 1 + 1 + 1
 *     2 + 2 + 1
 *     2 + 1 + 2
 *     1 + 2 + 2
 *     1 + 1 + 3
 *     1 + 3 + 1
 *     3 + 1 + 1
 *     2 + 3
 *     3 + 2
 */
