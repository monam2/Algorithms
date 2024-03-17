import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class BOJ_1303 {
	private static class Node {
		int x,y;

		public Node(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
	}//Node
	
	static int n, m, map[][];
	static boolean visitedW[][], visitedB[][];
	static ArrayDeque<Node> q;
	static int[] dx = {-1,0,1,0};
	static int[] dy = {0,1,0,-1};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		st = new StringTokenizer(br.readLine());
		
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		
		map = new int[n][m];
		for (int i = 0; i < n; i++) {
			String ipt = br.readLine();
			for (int j = 0; j < m; j++) {
				map[i][j] = ipt.charAt(j);
			}
		}
		
		visitedW = new boolean[n][m];
		visitedB = new boolean[n][m];
		int w = 0;
		int b = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 'W' && !visitedW[i][j]) {
					w += Math.pow(bfsW(i,j), 2);
				} else if (map[i][j] == 'B' && !visitedB[i][j]) {
					b += Math.pow(bfsB(i,j),2);
				}
			}
		}
		
		System.out.println(w + " " + b);
	}//main
	
	private static int bfsW(int x, int y) {
		q = new ArrayDeque<>();
		visitedW[x][y] = true;
		q.offer(new Node(x,y));
		int cnt = 1;
		
		while(!q.isEmpty()) {
			x = q.peek().x;
			y = q.poll().y;
			
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				if (0<=nx&&nx<n && 0<=ny&&ny<m && !visitedW[nx][ny] && map[nx][ny]=='W') {
					q.offer(new Node(nx,ny));
					visitedW[nx][ny] = true;
					cnt++;
				}
			}
		}
		
		return cnt;
		
	}//bfsW
	
	private static int bfsB(int x, int y) {
		q = new ArrayDeque<>();
		visitedB[x][y] = true;
		q.offer(new Node(x,y));
		int cnt = 1;
		
		while(!q.isEmpty()) {
			x = q.peek().x;
			y = q.poll().y;
			
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				if (0<=nx&&nx<n && 0<=ny&&ny<m && !visitedB[nx][ny] && map[nx][ny]=='B') {
					q.offer(new Node(nx,ny));
					visitedB[nx][ny] = true;
					cnt++;
				}
			}
		}
		
		return cnt;
		
	}//bfsB
}//class
