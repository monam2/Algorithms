import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main_10026 {
	/*
	 * 적록색약 bfs와 정상 bfs를 나누어서 진행
	 * blindBfs / normalBfs
	 */
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static int n, blind, normal;
	static int[] dx = {-1,0,1,0};
	static int[] dy = {0,1,0,-1};
	static char map[][];
	static boolean blindVisit[][], normalVisit[][];
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());

		map = new char[n][n];
		for (int i = 0; i < map.length; i++) {
			map[i] = br.readLine().toCharArray();
		}
		blindVisit = new boolean[n][n];
		normalVisit = new boolean[n][n];

		blind = 0;
		normal = 0;
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map.length; j++) {

				if (!blindVisit[i][j]) {
					blindVisit[i][j] = true;
					blindBfs(i,j);
					blind++;
				}
				if (!normalVisit[i][j]) {
					normalVisit[i][j] = true;
					normalBfs(i, j);
					normal++;
				}


			}
		}

		System.out.println(normal + " " + blind);


	}//end main

	private static void blindBfs(int x, int y) {
		ArrayDeque<int[]> q = new ArrayDeque<>();
		q.add(new int[] {x, y});
		while (!q.isEmpty()) {
			int[] tempArr = q.pollFirst();
			x = tempArr[0];
			y = tempArr[1];

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (0<=nx&&nx<n && 0<=ny&&ny<n && !blindVisit[nx][ny]) {
					//현재 칸이 R/G 이고 다음 칸도 R/G 라면 -> 적록색맹이니까
					if ((map[x][y]=='R' || map[x][y]=='G') && (map[nx][ny]=='R' || map[nx][ny]=='G')) {
						q.add(new int[] {nx, ny});
						blindVisit[nx][ny] = true;
					}
					else if (map[x][y]=='B' && map[nx][ny]=='B') {
						q.add(new int[] {nx, ny});
						blindVisit[nx][ny] = true;
					}
				}
			}
		}
	}//end blindBfs

	private static void normalBfs(int x, int y) {
		ArrayDeque<int[]> q = new ArrayDeque<>();
		q.add(new int[] {x, y});
		while (!q.isEmpty()) {
			int[] tempArr = q.pollFirst();
			x = tempArr[0];
			y = tempArr[1];

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (0<=nx&&nx<n && 0<=ny&&ny<n && !normalVisit[nx][ny]) {
					if (map[nx][ny]==map[x][y]) {
						q.add(new int[] {nx, ny});
						normalVisit[nx][ny] = true;
					}
				}
			}
		}
	}//end normalBfs

}//end class
