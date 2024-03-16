import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_2638 {
	private static class Node{
		int x,y;

		public Node(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
	}//Node
	
	static int n, m, map[][], contact[][];
	static boolean visited[][];
	static ArrayList<Node> removeList;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		map = new int[n][m];
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				int ipt = Integer.parseInt(st.nextToken());
				map[i][j] = ipt;
			}
		}
		
		// @Method : bfs()
		//BFS 탐색을 통해 지울 치즈의 갯수 체크
		// - 0인 지점을 통해서 이동하며 탐색
		// - 만약 1(치즈)? -> contact[nx][ny]++
		
		// @Method : searchContact_AddList()
		//visited를 순회하며 만약 contact[i][j] >= 2 라면
		//그 지점의 좌표를 리스트에 넣기.
		
		// @Method : melt()
		//위에서 넣은 리스트의 좌표들을 돌며 치즈 지우기
		
		// @Method : confirm()
		//map을 돌며 남은 치즈가 있는지 확인
		// 남은 치즈가 없으면 -> break
		int time = 1;
		while (true) {
			visited = new boolean[n][m];
			contact = new int[n][m];
			removeList = new ArrayList<Node>();
			
			bfs();
			searchContact_AddList();
			melt();
			
			if (confirm()) break;
			
			time++;
		}
		
		System.out.println(time);
	}//main
	
	private static void bfs() {
		ArrayDeque<Node> q = new ArrayDeque<Node>();
		q.offer(new Node(0,0));
		visited[0][0] = true;
		
		int[] dx = new int[] {-1,0,1,0};
		int[] dy = new int[] {0,1,0,-1};
		
		while (!q.isEmpty()) {
			int x = q.peek().x;
			int y = q.poll().y;
			
			for (int d = 0; d < 4; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				
				if (0<=nx&&nx<n && 0<=ny&&ny<m) {
					if (!visited[nx][ny] && map[nx][ny] == 0) {
						q.offer(new Node(nx,ny));
						visited[nx][ny] = true;
					}
					else if (map[nx][ny] == 1) {
						contact[nx][ny]++;
					}
				}
			}
		}
	}//bfs
	
	private static void searchContact_AddList() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (contact[i][j] >= 2) {
					removeList.add(new Node(i,j));
				}
			}
		}
	}//searchContact_AddList
	
	private static void melt() {
		for (Node node : removeList) {
			map[node.x][node.y]--;
			if (map[node.x][node.y]<0) {
				map[node.x][node.y] = 0;
			}
		}
	}//melt
	
	private static boolean confirm() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j]==1) {
					return false;
				}
			}
		}
		return true;
	}//confirm
	
	
}//class
