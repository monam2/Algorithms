import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Main { //BOJ 14940 쉬운 최단거리
	private static class Node {
		int x, y;

		public Node(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}

	}// Node

	private static int n, m, map[][];
	private static boolean visited[][];
	private static int[] dx = { -1, 0, 1, 0 };
	private static int[] dy = { 0, 1, 0, -1 };

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		map = new int[n][m];
		visited = new boolean[n][m];

		int x = 0;
		int y = 0;

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 2) {
					x = i;
					y = j;
				} else if (map[i][j] == 0) {
					visited[i][j] = true;
				}
			}
		}

		bfs(x, y);

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] != 0 && !visited[i][j]) {
					System.out.print("-1 ");
				} else {
					System.out.print(map[i][j] + " ");
				}
			}
			System.out.println();
		}
	}// main

	private static void bfs(int x, int y) {
		ArrayDeque<Node> q = new ArrayDeque<Node>();
		visited[x][y] = true;
		map[x][y] = 0;
		q.add(new Node(x, y));

		while (!q.isEmpty()) {
			Node node = q.poll();
			x = node.x;
			y = node.y;

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (0 <= nx && nx < n && 0 <= ny && ny < m && map[nx][ny] != 0 && !visited[nx][ny]) {
					q.add(new Node(nx, ny));
					visited[nx][ny] = true;
					map[nx][ny] = map[x][y] + 1;
				}
			}
		}
	}// bfs
}// class
