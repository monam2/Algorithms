import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Solution_5656 { //SWEA 5656 벽돌깨기
	private static class Node {
		int x, y, k;

		public Node(int x, int y, int k) {
			super();
			this.x = x;
			this.y = y;
			this.k = k;
		}
	}// Node

	static int n, w, h, map[][], answer;
	static int[] dx = {-1,0,1,0};
	static int[] dy = {0,1,0,-1};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t < T + 1; t++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			h = Integer.parseInt(st.nextToken());

			map = new int[h][w];
			for (int i = 0; i < h; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < w; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			answer = Integer.MAX_VALUE;
			dfs(0, new int[n]);

			//남은 벽돌 갯수 체크
			
			System.out.println("#" + t + " " + answer);
		} // for T
	}// main

	private static void dfs(int idx, int[] arr) {
		if (idx == n) {
			// 공을 쏠 위치를 선택 : arr [2,2,3] 등

			int[][] copyMap = copyMap();
			for (int i = 0; i < n; i++) {
				ArrayDeque<Node> q = shootAtLoca(arr[i], copyMap);
				copyMap = bombByQ(q, copyMap);
				copyMap = remakeMap(copyMap);
			}

			//남은 벽돌 갯수 체크
			int result = checkMap(copyMap);
			answer = Math.min(answer, result);
			return;
		}
		for (int i = 0; i < w; i++) {
			arr[idx] = i;
			dfs(idx + 1, arr);
		}
	}// dfs

	private static int checkMap(int[][] copyMap) {
		int cnt = 0;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (copyMap[i][j] > 0) {
					cnt++;
				}
			}
		}
		return cnt;
	}//checkMap


	private static int[][] remakeMap(int[][] copyMap) {
		int[][] newMap = new int[h][w];

		for (int i = 0; i < w; i++) {
			Stack<Node> stack = new Stack<>();

			for (int j = 0; j < h; j++) {
				if (copyMap[j][i] != 0) {
					stack.add(new Node(j,i,copyMap[j][i]));
				}
			}

			for (int j = h-1; j > -1; j--) {
				if (stack.isEmpty()) {
					continue;
				}
				Node temp = stack.pop();
				newMap[j][i] = temp.k;
			}

		}
		return newMap;
	}//remakeMap

	private static int[][] copyMap() {
		int[][] newMap = new int[h][w];
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				newMap[i][j] = map[i][j];
			}
		}
		return newMap;
	}//copyMap

	private static int[][] bombByQ(ArrayDeque<Node> q, int[][] copyMap) {
		while (!q.isEmpty()) {
			Node temp = q.poll();
			int x = temp.x;
			int y = temp.y;
			int k = temp.k;

			//십자로 퍼져야 함
			int d = 1;
			int nx = 0;
			int ny = 0;
			while (d<k) {
				for (int i = 0; i < 4; i++) {
					nx = x + dx[i]*d;
					ny = y + dy[i]*d;

					if (0<=nx&&nx<h && 0<=ny&&ny<w) {
						if (copyMap[nx][ny] > 1) {
							q.offer(new Node(nx,ny,copyMap[nx][ny]));
							copyMap[nx][ny] = 0;
						} else if (copyMap[nx][ny] == 1) {
							copyMap[nx][ny] = 0;
						}
					}
				}
				d++;
			}
			copyMap[x][y] = 0;
		}
		return copyMap;
	}//bombByQ

	private static ArrayDeque<Node> shootAtLoca(int shootLocaY, int[][] copyMap) {
		int shootLocaX = 0;
		ArrayDeque<Node> q = new ArrayDeque<>();

		while (shootLocaX<h) {
			if (copyMap[shootLocaX][shootLocaY] == 0) {
				shootLocaX++;
			} else {
				q.offer(new Node(shootLocaX, shootLocaY, copyMap[shootLocaX][shootLocaY]));
				break;
			}
		}
		return q;
	}// shootAtLoca
}// class
