import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class BOJ_4458 {
	public static class Node {
		int x, y;

		public Node(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
		
	}
	
	private static int n, map[][], visited[][];
	private static ArrayDeque<Node> q;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		int t=1;
		while (true) {
			n = Integer.parseInt(br.readLine());
			if (n==0) break;
			map = new int[n][n];
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			bfs();
			System.out.println("Problem " + t + ": " + visited[n-1][n-1]);
			t++;
		}
	}//main
	
	private static void bfs() {
		q = new ArrayDeque<>();
		visited = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				visited[i][j] = Integer.MAX_VALUE;
			}
		}
		visited[0][0] = map[0][0];
		q.offer(new Node(0,0));
		
		int[] dx = {-1,0,1,0};
		int[] dy = {0,1,0,-1};
		
		while(!q.isEmpty()) {
			int x = q.peek().x;
			int y = q.poll().y;
			
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				if (0<=nx && nx<n && 0<=ny && ny<n) {
					if (visited[nx][ny] > visited[x][y] + map[nx][ny]) {
						visited[nx][ny] = visited[x][y] + map[nx][ny];
						q.offer(new Node(nx,ny));
					}
				}
			}
		}
		
		
	}//bfs
}//class
