//백준 15649 n과m1

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(nm => parseInt(nm));

// const input = require('fs').readFileSync('input.txt').toString().trim().split(' ');
// const [n, m] = [4, 4]
const n = input.shift();
const m = input.shift();

let result = '';

const visited = new Array(10).fill(false);
const arr = [];

function dfs(k) {
    if (k===m) {
        result += `${arr.join(' ')}\n`;
        return;
    }
    for (let i=1; i<n+1; i++) {
        if (visited[i]===true) continue;
        visited[i] = true;
        arr.push(i);
        dfs(k+1);
        arr.pop();
        visited[i] = false;
    }
}

dfs(0);

console.log(result.trim())