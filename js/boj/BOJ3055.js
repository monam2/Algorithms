//백준 3055 탈출

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [R, C] = input[0].split(" ").map(Number);
const map = input.slice(1).map((str) => str.trim().split(""));

const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

function solution() {
  const water = [];
  const dochi = [];

  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      if (map[i][j] == "*") {
        //물 차있는 곳
        water.push([i, j]);
      } else if (map[i][j] == "S") {
        //고슴도치 위치
        dochi.push([i, j]);
      }
    }
  }

  let result = bfs(water, dochi);
  return result > 0 ? result : "KAKTUS";
} //solution

function bfs(water, dochi) {
  let q = [];
  for ([a, b] of water) {
    //큐에 물 위치 넣기
    q.push([a, b, -1]);
  }
  q.push([...dochi[0], 0]); //큐에 고슴도치 위치 넣기

  while (q.length) {
    let [x, y, dist] = q.shift();

    //고슴도치가 비버굴에 닿으면 종료
    if (dist > -1 && map[x][y] == "D") {
      return dist;
    }

    for (let d = 0; d < 4; d++) {
      let nx = x + dx[d];
      let ny = y + dy[d];

      if (0 <= nx && nx < R && 0 <= ny && ny < C && map[nx][ny] != "X") {
        //물이고 다음칸이 돌이 아니고 비버굴도 아니면 이동
        if (dist == -1 && map[nx][ny] == "." && map[nx][ny] != "D") {
          q.push([nx, ny, -1]);
          map[nx][ny] = "*";
        } else if (dist > -1 && (map[nx][ny] == "." || map[nx][ny] == "D")) {
          if (map[nx][ny] == "D") {
            return dist + 1;
          }
          q.push([nx, ny, dist + 1]);
          map[nx][ny] = "S";
        }
      }
    }
  }
  return -1;
} //bfs

console.log(solution());
