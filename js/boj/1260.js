// 백준 1260 DFS와 BFS
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
//백준용 입력

// const input = require('fs').readFileSync('input.txt').toString().trim().split('\n');
//로컬용 입력
const [N, M, V] = input.shift().split(' ').map(Number);
const edges = input.map(v => v.split(' ').map(Number));

const graph = Array.from(Array(N+1), ()=> new Array().fill(0));
edges.forEach(arr=>{
    let [a, b] = arr;
    graph[a].push(b)
    graph[b].push(a)
})
graph.forEach(i=>{
    i.sort((a,b)=>b-a);
})

// DFS
const stack = [];
let visited = Array.from(Array(N+1).fill(false));
stack.push(V);

const dfsResult = [];
while (stack.length > 0) {
    x = stack.pop();
    if (visited[x]===false){
        visited[x] = true;
        dfsResult.push(x);
    }
    for (let i=0; i<graph[x].length; i++) {
        if (graph[graph[x][i]].length > 0 && visited[graph[x][i]]===false){
            stack.push(graph[x][i]);
        }
    }
}

//BFS
graph.forEach(i=>{
    i.sort((a,b)=> a-b);
})

const bfsResult = [];
const q = [];
q.push(V);
let visited2 = Array.from(Array(N+1).fill(false));
while (q.length>0){
    x = q.shift();
    if (visited2[x]===false) {
        bfsResult.push(x);
        visited2[x] = true;
    }
    for (let i=0;i<graph[x].length;i++){
        if (graph[graph[x][i]].length>0 && visited2[graph[x][i]]===false) {
            q.push(graph[x][i]);
        }
    }
}
console.log(dfsResult.join(' '));
console.log(bfsResult.join(' '));