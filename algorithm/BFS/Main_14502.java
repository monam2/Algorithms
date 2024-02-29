import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_14502 { //백준 14502 연구소
	
	private static class Node{
		int x,y;

		public Node(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}

		@Override
		public String toString() {
			return "Node [x=" + x + ", y=" + y + "]";
		}
		
	}//Node

	static int n, m, map[][], safetyAreaCnt;
	static ArrayList<Node> list;
	static ArrayList<Node> virus;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		map = new int[n][m];
		list = new ArrayList<Node>();
		virus = new ArrayList<Node>();
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j]==0) {
					list.add(new Node(i,j));
				} else if (map[i][j]==2) {
					virus.add(new Node(i,j));
				}
			}
		}
		//input
		safetyAreaCnt = 0;
		
		getComb(0, 0, new Node[3]);
		System.out.println(safetyAreaCnt);
	}//main
	
	private static void getComb(int idx, int start, Node[] arr) {
		if (idx==3) {
			generateWalltoMap(arr);
			return;
		}
		for (int i = start; i < list.size(); i++) {
			arr[idx] = list.get(i);
			getComb(idx+1, i+1, arr);
		}
	}//getComb
	
	private static int startBfs(int[][] newMap) {
		ArrayDeque<Node> q = new ArrayDeque<>();
		boolean[][] visited = new boolean[n][m];
		for (Node node : virus) {
			q.offer(node);
			visited[node.x][node.y] = true;
		}
		
		int[] dx = {-1,0,1,0};
		int[] dy = {0,1,0,-1};
		
		while (!q.isEmpty()) {
			int x = q.peek().x;
			int y = q.poll().y;
			
			for (int d = 0; d < 4; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				if (0<=nx&&0<=ny && nx<n&&ny<m && !visited[nx][ny] && newMap[nx][ny]==0) {
					q.add(new Node(nx,ny));
					visited[nx][ny] = true;
					newMap[nx][ny] = 2;
				}
			}
		}
    
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (newMap[i][j]==0) {
					cnt++;
				}
			}
		}
		return cnt;
	}//stratBfs

	private static void generateWalltoMap(Node[] arr) {
		int[][] newMap = copyMap();
		for (Node node : arr) { //뽑은 3개의 벽 세우기
			newMap[node.x][node.y] = 1;
		}
		
		int res = startBfs(newMap);
		if (res > safetyAreaCnt) {
			safetyAreaCnt = res;
		}
	}//generateWalltoMap
	
	private static int[][] copyMap() {
		int[][] newMap = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				newMap[i][j] = map[i][j];
			}
		}
		return newMap;
	}//copyMap
}//class
